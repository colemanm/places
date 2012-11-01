# Copyright 2011 Omniscale (http://omniscale.com)
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#   http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from imposm.mapping import (
  Options,
  Points, LineStrings, Polygons,
  String, Bool, Integer, OneOfInt,
  set_default_name_type, LocalizedName,
  WayZOrder, ZOrder, Direction,
  GeneralizedTable, UnionView,
  PseudoArea, meter_to_mapunit, sqr_meter_to_mapunit,
)

# # internal configuration options
# # uncomment to make changes to the default values
import imposm.config
# 
# # import relations with missing rings
imposm.config.import_partial_relations = False
# 
# # select relation builder: union or contains
imposm.config.relation_builder = 'contains'
# 
# # log relation that take longer than x seconds
# imposm.config.imposm_multipolygon_report = 60
# 
# # skip relations with more rings (0 skip nothing)
# imposm.config.imposm_multipolygon_max_ring = 0


# # You can prefer a language other than the data's local language
# set_default_name_type(LocalizedName(['name:en', 'int_name', 'name']))

db_conf = Options(
  # db='osm',
  host='localhost',
  port=5432,
  user='osm',
  password='osm',
  sslmode='allow',
  prefix='osm_new_',
  proj='epsg:900913',
)

address_tags = (
  ('addr:housenumber',String()),
  ('addr:housename', String()),
  ('addr:street', String()),
  ('addr:place', String()),
  ('addr:city', String()),
  ('addr:country', String()),
  ('addr:full', String()),
  ('addr:hamlet', String()),
  ('addr:subdistrict', String()),
  ('addr:district', String()),
  ('addr:province', String()),
  ('addr:state', String()),
)

places = Points(
  name = 'places',
  mapping = {
    'place': (
      'country',
      'state',
      'region',
      'county',
      'city',
      'town',
      'village',
      'hamlet',
      'suburb',
      'locality',
    ),
  },
  fields = (
    ('z_order', ZOrder([
      'country',
      'state',
      'region',
      'county',
      'city',
      'town',
      'village',
      'hamlet',
      'suburb',
      'locality',
    ])),
    ('population', Integer()),
  ),
)

buildings = Polygons(
  name = 'buildings',
  fields = address_tags,
  mapping = {
    'building': (
      '__any__',
    ),
  }
)

barrierpoints = Points(
  name = 'barrierpoints',
  mapping = {
    'barrier': (
      'block',
      'bollard',
      'cattle_grid',
      'chain',
      'cycle_barrier',
      'entrance',
      'horse_stile',
      'gate',
      'spikes',
      'lift_gate',
      'kissing_gate',
      'fence',
      'yes',
      'wire_fence',
      'toll_booth',
      'stile',
    )
  }
)

transportation = Points(
  name = 'transportation',
  fields = (
    ('ref', String()),
  ),
  mapping = {
    'railway': (
      'station',
      'tram_stop',
      'subway_entrance',
    ),
    'aeroway': (
      'aerodrome',
      'terminal',
      'helipad',
      'gate',
    ),
    'amenity': (
      'bicycle_parking',
      'bicycle_rental',
      'bus_station',
      'car_rental',
      'car_sharing',
      'car_wash',
      'ev_charging',
      'ferry_terminal',
      'fuel',
      'parking',
      'taxi',
    )
  }
)

entertainment = Points(
  name = 'entertainment',
  fields = address_tags,
  mapping = {
    'amenity': (
      'bar',
      'biergarten',
      'arts_centre',
      'cinema',
      'nightclub',
      'stripclub',
      'studio',
      'theatre',
    )
  }
)

education = Points(
  name = 'education',
  fields = address_tags,
  mapping = {
    'amenity': (
      'university',
      'school',
      'college',
      'kindergarten',
      'library',
    ),
})

food_and_drink = Points(
  name = 'food_and_drink',
  fields = address_tags,
  mapping = {
    'amenity': (
      'cafe',
      'food_court',
      'ice_cream',
      'fast_food',
      'pub',
      'restaurant',
    )
  }
)

leisure = Points(
  name = 'leisure',
  fields = address_tags,
  mapping = {
    'leisure': (
      'beach_resort',
      'common',
      'dance',
      'dog_park',
      'fishing',
      'garden',
      'golf_course',
      'ice_rink',
      'marina',
      'miniature_golf',
      'nature_reserve',
      'park',
      'pitch',
      'playground',
      'slipway',
      'sports_centre',
      'stadium',
      'swimming_pool',
      'track',
      'water_park',
    )
  }
)

offices = Points(
  name = 'offices',
  fields = address_tags,
  mapping = {
    'office': (
      'accountant',
      'architect',
      'camping',
      'company',
      'educational_institution',
      'employment_agency',
      'estate_agent',
      'foundation',
      'government',
      'insurance',
      'it',
      'lawyer',
      'newspaper',
      'ngo',
      'political_party',
      'quango',
      'research',
      'telecommunication',
      'travel_agent',
    )
  }
)

outdoor = Points(
  name = 'outdoor',
  mapping = {
    'amenity': (
      'toilet',
      'bench',
      'fountain',
      'telephone',
      'waste_disposal',
      'waste_basket',
      'watering_place',
      'bbq',
      'drinking_water',
    )
  }
)

public_services = Points(
  name = 'public_services',
  fields = address_tags,
  mapping = {
    'amenity': (
      'fire_station',
      'police',
      'townhall',
      'social_facility',
      'nursing_home',
      'community_centre',
      'social_centre',
      'courthouse',
      'crematorium',
      'embassy',
      'grave_yard',
      'post_office',
      'prison',
      'public_building',
      'recycling',
      'shelter',
      'bank',
      'atm',
      'bureau_de_change',
    )
  }
)

medical = Points(
  name = 'medical',
  fields = address_tags,
  mapping = {
    'amenity': (
      'doctors',
      'dentist',
      'clinic',
      'pharmacy',
      'veterinary',
      'hospital',
    )
  }
)

shops = Points(
  name = 'shops',
  fields = address_tags,
  mapping = {
    'shop': (
      '__any__',
      # 'alcohol',
      # 'anime',
      # 'antiques',
      # 'art',
      # 'baby_goods',
      # 'bag',
      # 'bakery',
      # 'bathroom_furnishing',
      # 'beauty',
      # 'bed',
      # 'beverages',
      # 'bicycle',
      # 'books',
      # 'boutique',
      # 'butcher',
      # 'car',
      # 'car_parts',
      # 'car_repair',
      # 'carpet',
      # 'charity',
      # 'chemist',
      # 'clothes',
      # 'computer',
      # 'confectionery',
      # 'convenience',
      # 'copyshop',
      # 'curtain',
      # 'deli',
      # 'department_store',
      # 'dive',
      # 'doityourself',
      # 'dry_cleaning',
      # 'electronics',
      # 'erotic',
      # 'fabric',
      # 'farm',
      # 'florist',
      # 'frame',
      # 'funeral_directors',
      # 'furnace',
      # 'furniture',
      # 'garden_centre',
      # 'gas',
      # 'general',
      # 'gift',
      # 'glaziery',
      # 'greengrocer',
      # 'hairdresser',
      # 'hardware',
      # 'hearing_aids',
      # 'herbalist',
      # 'hifi',
      # 'hunting',
      # 'interior_decoration',
      # 'jewelry',
      # 'kiosk',
      # 'kitchen',
      # 'laundry',
      # 'mall',
      # 'massage',
      # 'mobile_phone',
      # 'money_lender',
      # 'motorcycle',
      # 'musical_instrument',
      # 'newsagent',
      # 'optician',
      # 'organic',
      # 'outdoor',
      # 'paint',
      # 'pawnbroker',
      # 'pet',
      # 'radiotechnics',
      # 'seafood or fish',
      # 'second_hand',
      # 'shoes',
      # 'sports',
      # 'stationery',
      # 'supermarket',
      # 'tattoo',
      # 'ticket',
      # 'tobacco',
      # 'toys',
      # 'trade',
      # 'user defined',
      # 'vacant',
      # 'vacuum_cleaner',
      # 'variety_store',
      # 'video',
      # 'window_blind',
      # 'drugstore',
    )
  }
)

addresses = UnionView(
  name = 'addresses',
  fields = address_tags,
  mappings = [transportation, education, entertainment, food_and_drink, leisure, public_services, medical]
)