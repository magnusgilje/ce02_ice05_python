import sys
import pytest
sys.path.insert(0,"..")
import get_weather_info

def test_weather_valid_params():
    myW = get_weather_info.Get_weather_info('AN')
    assert myW.description().find('WHAT') != -1
    assert myW.description().find('WHERE') != -1
    assert myW.description().find('WHEN') != -1
    assert myW.description().find('IMPACTS') != -1

def test_weather_description_pass_case1():

    myValidJson = {'features' : [
            {'properties' : {
                'description' : "some text"
            }
        }]}
    myDesc = get_weather_info.Get_weather_info('test').extract_weather_description(myValidJson)

    assert(myDesc == "some text")

def test_weather_description_pass_case2():
    '''
    Test we can cope if weather is ok
    '''
    myValidJson = {'features' : [] }

    myDesc = get_weather_info.Get_weather_info('AM').extract_weather_description(myValidJson)