import simplejson as simplejson
import requests
from datetime import datetime
from django.utils.timezone import make_aware

from django.conf import settings
from .models import Beer, Style, Category

BASE_URI='https://sandbox-api.brewerydb.com/v2/'
API_KEY=settings.BDB_API_KEY

PAYLOAD = {
    'key':API_KEY
}

max_total_retrieved = 50

# Example:
#https://sandbox-api.brewerydb.com/v2/beers/?key=

# Get all beers in the database
# Should probably change this to a method run every now and then to update the new beers, when it happnens (getting notifications of this from service, costs)
def getBeers():

    endpoint = 'beers/'
    result = requests.get(BASE_URI + endpoint, PAYLOAD).json()
    beers_in_total = int(result.get('totalResults'))
    print(beers_in_total)

    i = 0
    while i < max_total_retrieved:

        data = result['data'][i]
        i += 1
        style_dict = data.get('style')
        glass = data.get('glass')

        # New Style object
        if style_dict:
            category = style_dict.get('category')

            # New style category object
            if category:
                newCategory, created = Category.objects.get_or_create(
                    id = category.get('id'),
                    name = category.get('name')
                )
            else:
                newCategory = None

            newStyle, created = Style.objects.get_or_create(
                styleName = style_dict.get('name')
            )

            styleDescr_value = style_dict.get('description', '')
        else:
            newStyle = None
            styleDescr_value = ''

        # New beer object
        if data.get('isOrganic') == 'Y':
            isOrganic_value = True
        else:
            isOrganic_value = False

        if data.get('isRetired') == 'Y':
            isRetired_value = True
        else:
            isRetired_value = False

        if glass:
            glassName_value = glass.get('name')
        else:
            glassName_value = ''

        createDate_value = data.get('createDate')
        if createDate_value:
            createDate_value = datetime.strptime(createDate_value, '%Y-%m-%d %H:%M:%S')
            createDate_value = make_aware(createDate_value, None, True)

        updateDate_value = data.get('updateDate')
        if updateDate_value:
            updateDate_value = datetime.strptime(updateDate_value, '%Y-%m-%d %H:%M:%S')
            updateDate_value = make_aware(updateDate_value, None, True)

        newBeer = Beer(
            id = data.get('id'),
            name = data.get('name'),
            abv = data.get('abv'),
            style = newStyle,
            category = newCategory,
            isOrganic = isOrganic_value,
            isRetired = isRetired_value,
            createDate = createDate_value,
            updateDate = updateDate_value,
            glassName = glassName_value,
            styleDescription = styleDescr_value
        )
        newBeer.save()

    return result
