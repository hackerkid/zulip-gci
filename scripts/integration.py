import argparse
from upload import upload_task

parser = argparse.ArgumentParser()
parser.add_argument('--force', dest='force', action="store_true", default=False)
args = parser.parse_args()
if not args.force:
    print("Add --force argument to create tasks.")
    print("This is not idempotent. Running this twice with --force will create two sets of tasks.")
    exit(0)

integration_list = ['HelloSign', 'AppFollow', 'Mention', 'GoSquared', 'Mailchimp', 'InVision', 'Heroku', 'Stripe', 'Papertrail', 'Zeplin']
 
task_number = ['T0', 'T1', 'T2', 'T3']

beginner_tasks = ['T0', 'T1']

description = { 'T0' : """Start with this task to play around your favorite integration to Zulip!
 
This is a great way to learn the basics of python, git workflow and good style and understand how the integrations work with Zulip. You will also research and explore new things!
 
Instructions for integration tasks are at https://[TODO].""" }


for integration in integration_list:
    for task in ['T0']:
        upload_task(
            # https://developers.google.com/open-source/gci/resources/downloads/TaskAPISpec.pdf
            name = 'Create your own integration',
            description = description[task],
            status = 1, # 1: draft, 2: published
            max_instances = 1,
            mentors = ['niftynei@gmail.com', 'rishig@zulipchat.com', 'tabbott@zulipchat.com', 'reyhaverma@gmail.com'],
            tags = ['python', 'integration'], # free text
            # 1: Coding, 2: User Interface, 3: Documentation & Training,
            # 4: Quality Assurance, 5: Outreach & Research
            is_beginner = task in beginner_tasks,
            categories = [1, 4],
            time_to_complete_in_days = 4, # must be between 3 and 7
            # Field currently not accessible via API. gci-support says it is coming soon.
            # external_url = "TODO",
            private_metadata = "integration")

