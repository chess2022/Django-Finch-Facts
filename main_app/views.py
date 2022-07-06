# imports
from django.shortcuts import render
from django.http import HttpResponse

class Finch:
    def __init__(self, photo, name, region, description):
        self.photo = photo
        self.name = name
        self.region = region
        self.description = description

finches = [
    Finch('https://www.allaboutbirds.org/guide/assets/photo/306327341-720px.jpg','House Finch', 'North America', 'Adaptable, colorful, and cheery-voiced, House Finches are common from coast to coast today, familiar visitors to backyard feeders. Native to the Southwest, they are recent arrivals in the East. New York pet shop owners, who had been selling the finches illegally, released their birds in 1940 to escape prosecution; the finches survived, and began to colonize the New York suburbs. By 50 years later they had advanced halfway across the continent, meeting their western kin on the Great Plains.'),
    Finch('https://cdn.download.ams.birds.cornell.edu/api/v1/asset/256706671/1800', 'European Goldfinch', 'Europe to Central Asia', 'Beautiful little finch with a sharp pink bil, cherry-red face, and brilliant black-and-yellow flashes in the wings. Western birds (Europe east to far western Central Asia) have a black-and-white cowl; eastern birds (rest of Central Asia) lack this cowl, and are grayer overall, with more white on the wing. Juvenile (seen in late summer and autumn) has a plain head but is told easily by bold wing pattern. Uses a wide array of wooded and open habitats, from forests and gardens to steppe grasslands and meadows; often feeds on seeding thistles. Forms flocks in autumn and winter, gathering at food sources. Can be inconspicuous, but often detected by pleasant bubbling and twittering calls and song.'),
    Finch('https://cdn.download.ams.birds.cornell.edu/api/v1/asset/44585531/1800', 'Common Chaffinch', 'Europe to Asia, New Zealand', 'Common in varied wooded and forested habitats, parks, gardens, farmland with hedges and scattered trees. Forms flocks in winter; often visits garden feeders. Handsome, brightly colored male is distinctive, with bluish cowl, pink face and breast, black-and-white wing pattern (colors muted in winter). Female much drabber but shares male pattern; especially note the complex wing pattern. Both sexes have white outer tail feathers, often striking in flight such as when flushed.')
]

def home(request):
    return HttpResponse('<h1>Home is where the finches are</h1>')

def about(request):
    return render(request, 'about.html')

def finch_index(request):
    return render(request, 'finches/index.html', { 'finches': finches })