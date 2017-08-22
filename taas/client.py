import requests


class _BaseClient:
    def __init__(self, base_url, url_prefix):
        self._base_url = base_url
        self._url_prefix = url_prefix
        self.url = self._base_url + self._url_prefix

    def get_all(self):
        response = requests.get(self.url)
        return response.json()

    def get_by_id(self, db_id):
        response = requests.get(self.url+'/{}'.format(db_id))
        return response.json()

    def create(self, data):
        response = requests.post(self.url, json=data)
        return response.json()

    def update(self, db_id, data):
        response = requests.put(self.url+'/{}'.format(db_id), json=data)
        return response.json()

    def delete(self, db_id):
        response = requests.delete(self.url+'/{}'.format(db_id))
        return None


class TaasClient:
    def __init__(self, base_url):
        self.execution = _BaseClient(base_url, '/executions')
        self.execution_run = _BaseClient(base_url, '/execution-runs')
        self.parameter = _BaseClient(base_url, '/parameters')
        self.parameter_group = _BaseClient(base_url, '/parameter-groups')
        self.runner = _BaseClient(base_url, '/run')
        self.step = _BaseClient(base_url, '/steps')
        self.test_case = _BaseClient(base_url, '/test-cases')
        self.test_case_run = _BaseClient(base_url, '/test-runs')
        self.test_suite = _BaseClient(base_url, '/test-suites')
        self.test_suite_run = _BaseClient(base_url, '/test-suite-runs')
