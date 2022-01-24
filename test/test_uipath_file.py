
import json
import pytest 

@pytest.fixture
def projectJson():
    with open('project.json','r') as f:
        prj = json.loads(f.read())
    yield prj

@pytest.fixture
def projectMain():
    with open('Main.xaml','r') as f:
        prj_main = f.read()
    yield prj_main

class TestUipath:
    def test_squence_names(self,projectMain):
        assert """Sequence DisplayName="Bohemian Rhapsody" """ in projectMain
    def test_dependecies(self,projectJson):
        dependencies = {'UiPath.Excel.Activities': '[2.9.3]', 'UiPath.Mail.Activities': '[1.9.3]', 'UiPath.System.Activities': '[20.10.1]', 'UiPath.UIAutomation.Activities': '[20.10.6]'}
        for key in dependencies:
            assert dependencies[key] == projectJson['dependencies'][key]
    def test_verison(self,projectJson):
        options = {  "schemaVersion": "4.0",
                     "studioVersion": "20.10.2.0",
                     "projectVersion": "1.0.0"}
        for key in options:
            assert options[key] == projectJson[key]
