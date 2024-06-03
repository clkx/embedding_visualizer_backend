from fastapi import FastAPI
import os
from dotenv import load_dotenv
import pymongo
from bson import json_util
import json
from sklearn.decomposition import PCA
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

load_dotenv()
app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

MONGO_URL = os.getenv("MONGO_URL")
myclient = pymongo.MongoClient(MONGO_URL)
mydb = myclient["mydatabase"]
mycol = mydb["embedded_music"]

@app.get("/all")
def find_all():
    cursor = mycol.find({}, {"_id": 0, "name": 1, "genre": 1, "prompt": 1, "embedded_prompt": 1})
    results = list(cursor)
    
    # Extract embedded prompts from results
    embedded_prompts = [item['embedded_prompt'] for item in results if 'embedded_prompt' in item]

    # Dimensionality reduction to 3D
    if embedded_prompts:
        pca = PCA(n_components=3)
        embedding_3d = pca.fit_transform(embedded_prompts)

        # Add reduced dimensions to results and remove the original embedding
        for item, coords in zip(results, embedding_3d):
            item['umap_3d'] = coords.tolist()
            del item['embedded_prompt']  # Remove the original embedding

    return json.loads(json_util.dumps(results))

@app.get("/fixed")
def find_all():

    return [
  {
    "name": "A soothing classical piece with a gentle piano",
    "genre": "Classical",
    "prompt": "A soothing classical piece with a gentle piano",
    "umap_3d": [
      0.3205253141146796,
      0.0065327609787536114,
      -0.3007908996167041
    ]
  },
  {
    "name": " Soulful piano song with relaxing beats",
    "genre": "Blues",
    "prompt": " Soulful piano song with relaxing beats",
    "umap_3d": [
      -0.030949787727197194,
      0.26622328518528693,
      -0.19345116023941192
    ]
  },
  {
    "name": "jazz song with  Funky Backbeat",
    "genre": "Disco",
    "prompt": "jazz song with  Funky Backbeat",
    "umap_3d": [
      -0.24931326296132714,
      0.6647446534764688,
      0.19556837353012196
    ]
  },
  {
    "name": "jazz song with  Funky Backbeat",
    "genre": "Hip-hop",
    "prompt": "jazz song with  Funky Backbeat",
    "umap_3d": [
      -0.2493132629613272,
      0.6647446534764688,
      0.19556837353012224
    ]
  },
  {
    "name": "Create a laid-back reggae track that captures the vibe of a sunny beach ",
    "genre": "Hip-hop",
    "prompt": "Create a laid-back reggae track that captures the vibe of a sunny beach ",
    "umap_3d": [
      -0.2870769600725933,
      0.016967162792907203,
      -0.07612713305094662
    ]
  },
  {
    "name": "Create a smooth jazz piece reminiscent of a late-night lounge",
    "genre": "Blues",
    "prompt": "Create a smooth jazz piece reminiscent of a late-night lounge",
    "umap_3d": [
      -0.2036358276003567,
      0.2517203985647737,
      -0.11433573810394092
    ]
  },
  {
    "name": " Funky Backbeat Soulful Saxophone Solo Mystical meditation",
    "genre": "Pop",
    "prompt": " Funky Backbeat Soulful Saxophone Solo Mystical meditation",
    "umap_3d": [
      -0.10913517904977485,
      0.33602972691818045,
      -0.1743200862468387
    ]
  },
  {
    "name": " cartoon  Ocean Laid-back Shuffle cyberpunk dystopia",
    "genre": "Disco",
    "prompt": " cartoon  Ocean Laid-back Shuffle cyberpunk dystopia",
    "umap_3d": [
      -0.2822153997626536,
      -0.30082356399759314,
      0.5444477256715
    ]
  },
  {
    "name": "Classical Symphony Opus",
    "genre": "Classical",
    "prompt": "Compose a grand classical symphony opus that showcases the full range of orchestral instruments",
    "umap_3d": [
      0.5059640341807915,
      -0.11526094591403327,
      0.23909722019762375
    ]
  },
  {
    "name": " Mystical meditation Medieval Feast staccacato Laid-back Shuffle citypop",
    "genre": "Jazz",
    "prompt": " Mystical meditation Medieval Feast staccacato Laid-back Shuffle citypop",
    "umap_3d": [
      -0.15479501907343668,
      -0.18766200062641217,
      0.03785592060298203
    ]
  },
  {
    "name": "dsdsdsds",
    "genre": "Disco",
    "prompt": "dsdsdsds",
    "umap_3d": [
      -0.13078090885186008,
      -0.12327235616486976,
      0.5132888412523744
    ]
  },
  {
    "name": "jazz song with  Funky Backbeat",
    "genre": "Disco",
    "prompt": "jazz song with  Funky Backbeat",
    "umap_3d": [
      -0.24931326296132714,
      0.6647446534764688,
      0.19556837353012252
    ]
  },
  {
    "name": "jazz song with  Funky Backbeat",
    "genre": "Hip-hop",
    "prompt": "jazz song with  Funky Backbeat",
    "umap_3d": [
      -0.2493132629613272,
      0.664744653476469,
      0.1955683735301226
    ]
  },
  {
    "name": "jazz song with  Funky Backbeat",
    "genre": "Hip-hop",
    "prompt": "jazz song with  Funky Backbeat",
    "umap_3d": [
      -0.24931326296132714,
      0.6647446534764687,
      0.19556837353012252
    ]
  },
  {
    "name": "Classical Piano Etude",
    "genre": "Classical",
    "prompt": "Compose a classical piano etude that challenges pianists with its technical demands and expressive melodies",
    "umap_3d": [
      0.5505650224695519,
      -0.08914011252084607,
      0.09719348413573548
    ]
  },
  {
    "name": "classical piano",
    "genre": "Classical",
    "prompt": "classical piano",
    "umap_3d": [
      0.66436861623456,
      0.03958635048002837,
      0.007171391805844379
    ]
  },
  {
    "name": "classical piano",
    "genre": "Classical",
    "prompt": "classical piano",
    "umap_3d": [
      0.66436861623456,
      0.03958635048002828,
      0.007171391805844358
    ]
  },
  {
    "name": "classical piano",
    "genre": "Classical",
    "prompt": "classical piano",
    "umap_3d": [
      0.66436861623456,
      0.03958635048002838,
      0.0071713918058443765
    ]
  },
  {
    "name": "classical piano",
    "genre": "Classical",
    "prompt": "classical piano",
    "umap_3d": [
      0.66436861623456,
      0.03958635048002831,
      0.007171391805844351
    ]
  },
  {
    "name": "classical music",
    "genre": "Jazz",
    "prompt": "classical music",
    "umap_3d": [
      0.5505650224695517,
      -0.08914011252084612,
      0.09719348413573552
    ]
  },
  {
    "name": "classical piano",
    "genre": "Classical",
    "prompt": "classical piano",
    "umap_3d": [
      0.66436861623456,
      0.03958635048002831,
      0.007171391805844335
    ]
  },
  {
    "name": "classical music",
    "genre": "Jazz",
    "prompt": "classical music",
    "umap_3d": [
      0.5505650224695517,
      -0.0891401125208461,
      0.09719348413573546
    ]
  },
  {
    "name": "classical music",
    "genre": "Classical",
    "prompt": "classical music",
    "umap_3d": [
      0.5505650224695517,
      -0.08914011252084617,
      0.09719348413573552
    ]
  },
  {
    "name": "classical music",
    "genre": "Classical",
    "prompt": "classical music",
    "umap_3d": [
      0.5505650224695517,
      -0.08914011252084605,
      0.09719348413573549
    ]
  },
  {
    "name": "classical music piano",
    "genre": "Classical",
    "prompt": "classical music piano",
    "umap_3d": [
      0.6639534330858506,
      0.046405320815671156,
      -0.022055814249570576
    ]
  },
  {
    "name": "classical music violin",
    "genre": "Classical",
    "prompt": "classical music violin",
    "umap_3d": [
      0.4738938920581035,
      -0.01751441210401493,
      0.08213324036012598
    ]
  },
  {
    "name": "jazz song with  Soulful Saxophone Solo",
    "genre": "Pop",
    "prompt": "jazz song with  Soulful Saxophone Solo",
    "umap_3d": [
      -0.08066241526939213,
      0.4872189642315488,
      -0.18583641913390173
    ]
  },
  {
    "name": "Retro video game music with  Soulful Saxophone Solo",
    "genre": "Blues",
    "prompt": "Retro video game music with  Soulful Saxophone Solo",
    "umap_3d": [
      -0.0016898922804992568,
      0.24929205310511365,
      -0.0661930792600736
    ]
  },
  {
    "name": "disco song background music",
    "genre": "Disco",
    "prompt": "",
    "umap_3d": [
      -0.2003166474983722,
      -0.1042803348490433,
      0.527143500540547
    ]
  },
  {
    "name": "Relaxing jazz song background music",
    "genre": "Pop",
    "prompt": "Relaxing jazz song background music",
    "umap_3d": [
      -0.12120970108863285,
      0.40847108245629776,
      -0.15779039055377256
    ]
  },
  {
    "name": "Relaxing jazz song background music",
    "genre": "Jazz",
    "prompt": "Relaxing jazz song background music",
    "umap_3d": [
      -0.12120970108863276,
      0.4084710824562978,
      -0.15779039055377245
    ]
  },
  {
    "name": "A cheerful country tune with bright guitars and happy harmonica",
    "genre": "Blues",
    "prompt": "A cheerful country tune with bright guitars and happy harmonica",
    "umap_3d": [
      -0.09209865833729304,
      0.14855369843074123,
      -0.2641749988979121
    ]
  },
  {
    "name": "A cheerful blues track with a lively guitar and upbeat rhythm",
    "genre": "Hip-hop",
    "prompt": "A cheerful blues track with a lively guitar and upbeat rhythm",
    "umap_3d": [
      -0.1561822332052798,
      0.12208447875748399,
      -0.05767527771975818
    ]
  },
  {
    "name": "A vibrant jazz piece with lively saxophone and upbeat piano",
    "genre": "Pop",
    "prompt": "A vibrant jazz piece with lively saxophone and upbeat piano",
    "umap_3d": [
      0.0716414378650054,
      0.3367464165797157,
      -0.20076412152721296
    ]
  },
  {
    "name": "A festive rock anthem with lively riffs and merry vocals",
    "genre": "Jazz",
    "prompt": "A festive rock anthem with lively riffs and merry vocals",
    "umap_3d": [
      -0.16575378727837697,
      -0.05053430734531209,
      -0.065583782681603
    ]
  },
  {
    "name": "An energetic pop song with happy lyrics and positive melodies",
    "genre": "Hip-hop",
    "prompt": "An energetic pop song with happy lyrics and positive melodies",
    "umap_3d": [
      -0.2241655162971083,
      0.04222322314307194,
      -0.07428425792294267
    ]
  },
  {
    "name": "Midnight Jazz Escape",
    "genre": "Classical",
    "prompt": "A bright classical composition with uplifting strings and vibrant piano",
    "umap_3d": [
      0.29897911283477346,
      -0.0031053267782300943,
      -0.16767127757789246
    ]
  },
  {
    "name": "Create a hauntingly beautiful melody with ethereal vocals.",
    "genre": "Country",
    "prompt": "Create a hauntingly beautiful melody with ethereal vocals.",
    "umap_3d": [
      -0.23371355612689335,
      -0.17914119031869732,
      -0.23514903538754747
    ]
  },
  {
    "name": "Craft a high-energy track perfect for a workout playlist",
    "genre": "Metal",
    "prompt": "Craft a high-energy track perfect for a workout playlist",
    "umap_3d": [
      -0.2047743824573924,
      -0.08736736952550127,
      0.2299060014752475
    ]
  },
  {
    "name": "Compose a melancholic piano piece that evokes feelings of longing and nostalgia",
    "genre": "Rock",
    "prompt": "Compose a melancholic piano piece that evokes feelings of longing and nostalgia",
    "umap_3d": [
      0.08367031989879861,
      -0.12415147890695163,
      -0.2938087212330923
    ]
  },
  {
    "name": "Imagine a futuristic soundscape with pulsating electronic beats and synthetic textures",
    "genre": "Metal",
    "prompt": "Imagine a futuristic soundscape with pulsating electronic beats and synthetic textures",
    "umap_3d": [
      -0.19827440703292015,
      -0.2212976076667008,
      0.2269418309913978
    ]
  },
  {
    "name": "Capture the essence of a thunderstorm in a piece of music, with crashing percussion and rumbling bass",
    "genre": "Jazz",
    "prompt": "Capture the essence of a thunderstorm in a piece of music, with crashing percussion and rumbling bass",
    "umap_3d": [
      -0.20459237605993089,
      -0.147179231222941,
      0.011633748775895677
    ]
  },
  {
    "name": "Create a whimsical soundtrack for an imaginary adventure through a magical forest",
    "genre": "Country",
    "prompt": "Create a whimsical soundtrack for an imaginary adventure through a magical forest",
    "umap_3d": [
      -0.1761236755660375,
      -0.24437246384039982,
      -0.218384016485878
    ]
  },
  {
    "name": "Imagine a romantic evening under the stars and compose the soundtrack for it",
    "genre": "Rock",
    "prompt": "Imagine a romantic evening under the stars and compose the soundtrack for it",
    "umap_3d": [
      -0.07513490939917578,
      -0.2170710747432042,
      -0.1850353344670483
    ]
  },
  {
    "name": "Craft a mysterious and suspenseful composition that keeps listeners on the edge of their seats",
    "genre": "Jazz",
    "prompt": "Craft a mysterious and suspenseful composition that keeps listeners on the edge of their seats",
    "umap_3d": [
      -0.16800614711190734,
      -0.3007741931823399,
      -0.037880176922039356
    ]
  },
  {
    "name": "Compose a regal fanfare fit for a royal procession",
    "genre": "Rock",
    "prompt": "Compose a regal fanfare fit for a royal procession",
    "umap_3d": [
      -0.1582168008149894,
      -0.362404954810553,
      0.09493638473178057
    ]
  },
  {
    "name": "Capture the chaos of a bustling city street with a cacophony of urban sounds",
    "genre": "Metal",
    "prompt": "Capture the chaos of a bustling city street with a cacophony of urban sounds",
    "umap_3d": [
      -0.25671547138756134,
      -0.20878008675789247,
      0.15754478678609932
    ]
  },
  {
    "name": "Capture the spirit of a roaring bonfire with rhythmic percussion and crackling sounds",
    "genre": "Reggae",
    "prompt": "Capture the spirit of a roaring bonfire with rhythmic percussion and crackling sounds",
    "umap_3d": [
      -0.3475062140427252,
      -0.21190398293584992,
      -0.0633749213705776
    ]
  },
  {
    "name": "Craft a dreamy electronic track that takes listeners on a journey through cyberspace",
    "genre": "Metal",
    "prompt": "Craft a dreamy electronic track that takes listeners on a journey through cyberspace",
    "umap_3d": [
      -0.2995009575205734,
      -0.3176259048215882,
      0.22371319491487549
    ]
  },
  {
    "name": "Craft a relaxing ambient track perfect for meditation and mindfulness",
    "genre": "Jazz",
    "prompt": "Craft a relaxing ambient track perfect for meditation and mindfulness",
    "umap_3d": [
      -0.26597780108685787,
      -0.10515231330385999,
      -0.11861751166270196
    ]
  },
  {
    "name": "Create a mystical forest ambiance with soft whispers of wind and rustling leaves",
    "genre": "Country",
    "prompt": "Create a mystical forest ambiance with soft whispers of wind and rustling leaves",
    "umap_3d": [
      -0.3370450501190054,
      -0.2521903069700162,
      -0.2503522671240139
    ]
  },
  {
    "name": "Craft a pulsating EDM track that ignites the dancefloor with electrifying energy",
    "genre": "Metal",
    "prompt": "Craft a pulsating EDM track that ignites the dancefloor with electrifying energy",
    "umap_3d": [
      -0.2666519697344966,
      -0.22431425350493323,
      0.2434652303723043
    ]
  },
  {
    "name": "Compose a bittersweet melody that tells the story of lost love and redemption",
    "genre": "Rock",
    "prompt": "Compose a bittersweet melody that tells the story of lost love and redemption",
    "umap_3d": [
      -0.10077506076467457,
      -0.1948155477199539,
      -0.29813716002464113
    ]
  },
  {
    "name": "Capture the essence of a summer breeze in a light and airy acoustic guitar piece",
    "genre": "Country",
    "prompt": "Capture the essence of a summer breeze in a light and airy acoustic guitar piece",
    "umap_3d": [
      -0.27889667509470023,
      -0.16887601140755754,
      -0.20714526282953
    ]
  },
  {
    "name": "Craft an epic orchestral battle theme worthy of a heroic showdown",
    "genre": "Jazz",
    "prompt": "Craft an epic orchestral battle theme worthy of a heroic showdown",
    "umap_3d": [
      -0.0011937584925908334,
      -0.293902188571423,
      -0.007964682968713641
    ]
  },
  {
    "name": "Create a whimsical carnival atmosphere filled with laughter and joyous melodies",
    "genre": "Reggae",
    "prompt": "Create a whimsical carnival atmosphere filled with laughter and joyous melodies",
    "umap_3d": [
      -0.2720019535903571,
      -0.318846325262256,
      -0.09436693496795512
    ]
  },
  {
    "name": "Compose a hauntingly beautiful lullaby that soothes the soul and calms the mind",
    "genre": "Rock",
    "prompt": "Compose a hauntingly beautiful lullaby that soothes the soul and calms the mind",
    "umap_3d": [
      -0.16545425226990954,
      -0.13762228108731694,
      -0.393104994029164
    ]
  },
  {
    "name": "Imagine an underwater journey and craft the music to accompany the exploration",
    "genre": "Jazz",
    "prompt": "Imagine an underwater journey and craft the music to accompany the exploration",
    "umap_3d": [
      -0.15913900866237465,
      -0.2716543680377854,
      -0.02066981933786436
    ]
  },
  {
    "name": "Capture the thrill of a high-speed chase with adrenaline-pumping beats and intense rhythms",
    "genre": "Metal",
    "prompt": "Capture the thrill of a high-speed chase with adrenaline-pumping beats and intense rhythms",
    "umap_3d": [
      -0.21752123233328746,
      -0.170469751878637,
      0.28674263688331086
    ]
  },
  {
    "name": "Compose an enchanting fairy tale soundtrack filled with wonder and magic",
    "genre": "Country",
    "prompt": "Compose an enchanting fairy tale soundtrack filled with wonder and magic",
    "umap_3d": [
      -0.11966616196959871,
      -0.27565077693186707,
      -0.11704192513407034
    ]
  },
  {
    "name": "Capture the tranquility of a sun-drenched beach with gentle waves and seagull cries",
    "genre": "Reggae",
    "prompt": "Capture the tranquility of a sun-drenched beach with gentle waves and seagull cries",
    "umap_3d": [
      -0.37796996663250715,
      -0.2648772004063646,
      -0.09863891963348471
    ]
  }
]

@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run(app, port=8080, log_level="info")

