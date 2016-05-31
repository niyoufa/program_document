from django.core.management import call_command
import json
call_command('gearman_submit_job','send_email',json.dumps({
                'to':['niyoufa@tmlsystem.com'],
                'content':'niyoufa_content',
                'subject':'niyoufa_subject'
}),foreground=False)