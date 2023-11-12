import pytest
from film import FilmService

@pytest.fixture
def setup_data():
    store = [
    {'nome':'Amaliè', 'anno':2001, 'origine':'Francia'},
    {'nome':'Ora ci arrabbiamo', 'anno':2001, 'origine':'Italia'},
    {'nome':'Noi testiamo sempre', 'anno':2023, 'origine':'Svizzera'},
    {'nome':'Benvenuti all''Est', 'anno':2021, 'origine':'Francia'},
        ]
    print("\nSetting up resources...")
    yield store  # Provide the data to the test
    # Teardown: Clean up resources (if any) after the test
    print("\nTearing down resources...")

def test_invalid_input(setup_data):
    anno = None
    origine = None
    service = FilmService(setup_data)
    with pytest.raises(ValueError):
        service.get_film(anno, origine)

def test_per_anno_senza_output(setup_data):
    anno = '2022'
    origine = None
    expected = []
    fs = FilmService(setup_data)
    res = fs.get_film(anno, origine)
    assert res == expected 

def test_per_anno_un_output(setup_data):
    anno = 2021
    origine = None
    expected = [
         {'nome':'Benvenuti all''Est', 'anno':2021, 'origine':'Francia'}
         ]
    fs = FilmService(setup_data)
    res = fs.get_film(anno, origine)
    assert len(expected) == len(res)


def test_per_anno_output_multiplo(setup_data):
    anno = 2001
    origine = None
    expected = [
         {'nome':'Amaliè', 'anno':2001, 'origine':'Francia'},
         {'nome':'Ora ci arrabbiamo', 'anno':2001, 'origine':'Italia'}
         ]
    fs = FilmService(setup_data)
    res = fs.get_film(anno, origine)
    assert len(expected) == len(res)


@pytest.mark.parametrize("anno,origine,expected",[    
    (2022, None, []),
    (2024, None, []),
    (2021, None, [
        {'nome':'Benvenuti all''Est', 'anno':2021, 'origine':'Francia'}
        ]),
    (2001, None, [
        {'nome':'Amaliè', 'anno':2001, 'origine':'Francia'},
        {'nome':'Ora ci arrabbiamo', 'anno':2001, 'origine':'Italia'},
    ])
])
def test_film_per_anno(anno, origine, expected):
    # Come usare la fixture per evitare la creazione di store?
    store = [
    {'nome':'Amaliè', 'anno':2001, 'origine':'Francia'},
    {'nome':'Ora ci arrabbiamo', 'anno':2001, 'origine':'Italia'},
    {'nome':'Noi testiamo sempre', 'anno':2023, 'origine':'Svizzera'},
    {'nome':'Benvenuti all''Est', 'anno':2021, 'origine':'Francia'},
        ]    
    fs = FilmService(store)
    res = fs.get_film(anno, origine)
    assert len(expected) == len(res)