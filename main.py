def define_env(env):
    @env.macro
    def course_summary(title, date, level, mentors):

        site = env.conf["site_url"].strip("/")

        return f"""# {title}

| Key | Info |
|-----|-------|
| Created date | { date } |
| Level | { level } |
| Mentor{ 's' if len(mentors) > 1 else ''} | {''.join([f'<a href="{site}/contributing/#mentor-{mentor}"><img style="border-radius:50%;width:50px;height:50px;margin-right:8px;" src="https://github.com/{ mentor }.png"></a>' for mentor in mentors])} |
"""
