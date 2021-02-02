def define_env(env):
    @env.macro
    def course_summary(title, date, level, mentors, tags, links):

        site = env.conf["site_url"].strip("/")

        return f"""# {title}

| Key | Info |
|-----|-------|
| Created date | { date } |
| Level | { level } |
| Mentor{ 's' if len(mentors) > 1 else ''} | {''.join([f'<a href="{site}/contributing/#mentor-{mentor}"><img style="border-radius:50%;width:50px;height:50px;margin-right:8px;" src="https://github.com/{ mentor }.png"></a>' for mentor in mentors])} |
| Tag{ 's' if len(tags) > 1 else ''} | {''.join([f'<div style="background:var(--md-default-fg-color--light);float:left;margin-left:8px;padding:4px;color:var(--md-default-bg-color);margin-bottom:8px;border-radius:0.1rem;">{tag}</div>' for tag in tags])} |
| Link{ 's' if len(links) > 1 else ''} | {''.join([f'<div>{link}</div>' for link in links])} |

"""
