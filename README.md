## Places

Mapping script for [imposm](http://imposm.org/) for building POI tables in PostGIS from OpenStreetMap extracts.

    imposm -U postgres_user -d postgres_db -m imposm-places.py --read --write --optimize --deploy-production-tables data.osm.pbf
