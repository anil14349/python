from locust import HttpLocust, TaskSet, task


class TemplateLoadTest(TaskSet):

    @task(5)
    def preview_template(self):
        response = self.client.request(method="POST",
                                       url="/epic",
                                       headers={
                                           "Content-Type": "text/plain"
                                       },
                                       data={
                                           """MSH|^~\&|EPIC||||20170912114704|GARDEJ04|ADT^A04|43400|T|2.3
                                           EVN|A04|20170912114704||AS_AFTER_CHECK_IN|GARDEJ04^GARDENHIRE^JULIE^^^^^^NYUSA^^^^^HJD
                                           PID|1|10025194^^^NYU MRN^MRN|10025194^^^NYU MRN^MRN||SALESFORCE^OUTPATIENT|SMITH|19971131|M||W|1234 WEST BROADWAY^^NEW YORK^NY^10011^US^^^60|60|(608)999-5454^HOME^PH^^^608^9995454~^NET^Internet^op@epic.com~(608)444-1212^HOME^CP^^^608^4441212|(608)444-6565^HOME^PH^^^608^4446565|ENGLISH|M|EPISCOPAL||524778989|||N||||||||N
                                           PD1|||HOSPITAL FOR JOINT DISEASES^^HJD|1821294034^ADLER^NICOLE^^^^^^EPIC^^^^PNPI
                                           CON|1|HIE Status
                                           NK1|1|SALESFORCE^MINNIE|SPOUSE|1234 West Broadway^^NEW YORK^NY^10011^US|(608)999-5454^^PH^^^608^9995454|(608)555-2323^^PH^^^608^5552323|EMC1
                                           PV1|1|O|TCRIM^^^TRINITY^^^^^^^DEPID|EL||||||||||Phys Ref|||||496686253|MANAGED CARE||||||||||||||||||||||||20170912114701
                                           PV2||||||||20170912121500||||FOLLOW UP||||||||||N
                                           GT1|1|2528594|SALESFORCE^OUTPATIENT||1234 WEST BROADWAY^^NEW YORK^NY^10011^US^^^60|(608)999-5454^^^^^608^9995454|(608)444-6565^^^^^608^4446565|19970912|M|Personal/Family|SLF|524778989||||1199 NATIONAL BENEFIT FUND|330 WEST 42ND STREET^^NEW YORK^NY^10036^US|(646)473-9200^^^^^646^4739200||Full
                                           IN1|1|CAE^AETNA HMO^PBPLAN~AETHMO^AETNA HMO^HBPLAN|1131|AETNA HMO|PO BOX 981106^^EL PASO^TX^79998-1106|||444444|||||||Managed Care|SALESFORCE^OUTPATIENT|Self|19970912|1234 WEST BROADWAY^^NEW YORK^NY^10011^US^^^60|||1|||YES||||||||||4169212|9084446354||||||Full|M|330 WEST 42ND STREET^^NEW YORK^NY^10036^US|||PPO
                                           IN2||524778989|||Payor Plan||||||||||||||||||||||||||||||||||||||||||||||||||||||||9084446354||(608)999-5454^^^^^608^9995454|(646)473-9200^^^^^646^4739200||||||1199 NATIONAL BENEFIT FUND"""
                                       })
        print("Preview; Response status code:", response.status_code)


class WebsiteUser(HttpLocust):
    host = 'https://nyu-patientadtjsonintegration-sit.cloudhub.io'
    task_set = TemplateLoadTest
    min_wait = 5000
    max_wait = 9000
