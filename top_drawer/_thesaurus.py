import aiohttp

API_URL_TEMPLATE = 'https://words.bighugelabs.com/api/2/{api_key}/{word}/json'

NOUN = 'noun'
VERB = 'verb'

SYNONYM = 'syn'
ANTONYM = 'ant'
USR = 'usr'  # Not really sure what this is.
ALL = 'all'

WORD_TYPES = (
    NOUN,
    VERB,
    ALL
)


async def thesaurus(session: aiohttp.ClientSession, api_key: str, word: str):
    url = API_URL_TEMPLATE.format(api_key=api_key, word=word)
    data = {}
    async with session.get(url) as response:  # type: aiohttp.ClientResponse

        if response.status == 200:
            data = await response.json(content_type='text/javascript')
        elif response.status != 404:
            response.raise_for_status()

    return data


def reduce_thesaurus(
        data: dict, word_type: str, include_antonyms: bool, include_usr: bool
):
    thes = set()
    for category, word_data in data.items():
        if word_type == ALL or category == word_type:
            thes.update(word_data.get(SYNONYM, []))
            if include_antonyms:
                thes.update(word_data.get(ANTONYM, []))
            if include_usr:
                thes.update(word_data.get(USR, []))

    return thes
