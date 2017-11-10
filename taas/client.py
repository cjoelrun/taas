import requests


class _BaseClient:
    def __init__(self, base_url, url_prefix):
        self._base_url = base_url
        self._url_prefix = url_prefix
        self.url = self._base_url + self._url_prefix

    def get_all(self):
        response = requests.get(self.url)
        return response.json()

    def get(self, **kwargs):
        print(kwargs)
        response = requests.get(self.url, params=kwargs)
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


class _RunnerClient:
    def __init__(self, base_url):
        self._base_url = base_url

    def run_test_case(self, case_id, parameter_id):
        response = requests.post(self._base_url+'/run/test-cases/{}'.format(case_id), json={'parameter_id': parameter_id})
        return response.json()

    def run_test_suite(self, case_id, parameter_id):
        response = requests.post(self._base_url+'/run/test-suites/{}'.format(case_id), json={'parameter_id': parameter_id})
        return response.json()

    def finish_test_suites(self):
        response = requests.post(self._base_url+'/run/test-suites/finish')
        return

    def cancel_test_case_run(self, case_run_id):
        response = requests.post(self._base_url+'/run/test-case-runs/{}/cancel'.format(case_run_id))
        return response.json()

    def cancel_test_suite_run(self, suite_run_id):
        response = requests.post(self._base_url + '/run/test-suite-runs/{}/cancel'.format(suite_run_id))
        return response.json()


class TaasClient:
    def __init__(self, base_url):
        self.execution = _BaseClient(base_url, '/executions')
        self.execution_run = _BaseClient(base_url, '/execution-runs')
        self.parameter = _BaseClient(base_url, '/parameters')
        self.parameter_group = _BaseClient(base_url, '/parameter-groups')
        self.runner = _RunnerClient(base_url)
        self.step = _BaseClient(base_url, '/steps')
        self.test_case = _BaseClient(base_url, '/test-cases')
        self.test_case_run = _BaseClient(base_url, '/test-runs')
        self.test_suite = _BaseClient(base_url, '/test-suites')
        self.test_suite_run = _BaseClient(base_url, '/test-suite-runs')
