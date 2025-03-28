import query
from dotenv import load_dotenv
from twitter import Twitter
from csvwriter import CSVWriter
import os
import out
import twitter


load_dotenv()
output_dir = os.getenv('PNG_OUTPUT', './out')

def init_twitter():
    ck = os.getenv('TWITTER_CONSUMER_KEY', None)
    cs = os.getenv('TWITTER_CONSUMER_SECRET', None)
    at = os.getenv('TWITTER_ACCESS_TOKEN', None)
    ats = os.getenv('TWITTER_ACCESS_TOKEN_SECRET', None)
    if ck == None or cs == None or at == None or ats == None:
        raise Exception('Twitter creds not defined')
    return Twitter(ck, cs, at, ats)

def init_csv():
    csvdir = os.getenv('CSV_DIR', None)
    perfile = os.getenv('CSV_OBJECTS_PER_FILE', None)
    if csvdir == None or perfile == None:
        raise Exception('CSV variables not defined')
    return CSVWriter(csvdir, 'batch', perfile)

search_radius = os.getenv('SEARCH_RADIUS', 0.1)

tw_client = init_twitter()
csv_writer = init_csv()

while True:
    objects = query.get_objects_in_radius()
    if len(objects) == 0:
        print("No TESS objects found within the specified radius.")
        continue;
    print("Found %u objects", len(objects))
    for name in objects:
        sets = query.search(name)
        if len(sets) == 0:
            print("Empty set for id: %s", name)
            continue;
        csv_writer.write_row({"TIC_ID": sets[0].id})
    files = out.read(output_dir)
    for data in files:
        tw_client.tweet(data['target_id'], [data['tpf'], data['lc'], data['phase']])
    
    
    




