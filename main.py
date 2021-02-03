def define_env(env):
    @env.macro
    def course_summary(title, date, level, mentors, tags, links, problems):

        site = env.conf["site_url"].strip("/")

        return f"""# {title}

| Key | Info |
|-----|-------|
| Created date | { date } |
| Level | { level } |
| Mentor{ 's' if len(mentors) > 1 else ''} | {''.join([f'<a href="{site}/contributing/#mentor-{mentor}"><img style="border-radius:50%;width:50px;height:50px;margin-right:8px;" src="https://github.com/{ mentor }.png"></a>' for mentor in mentors])} |
| Tag{ 's' if len(tags) > 1 else ''} | {''.join([f'<div style="background:var(--md-default-fg-color--light);float:left;margin-left:8px;padding:4px;color:var(--md-default-bg-color);margin-bottom:8px;border-radius:0.1rem;">{tag}</div>' for tag in tags])} |
| Link{ 's' if len(links) > 1 else ''} | {''.join([f'<div>{link}</div>' for link in links])} |
| Follow along problems{ 's' if len(problems) > 1 else ''} | {''.join([f'<div>{problem}</div>' for problem in problems])} |

"""

    @env.macro
    def mentor_summary(mentor):

        site = env.conf["site_url"].strip("/")

        return f"""
        <div id="mentor-{ mentor['github'] }" style="display: flex;margin-bottom:30px;">
            <img style="border-radius:50%;width:80px;height:80px" src="https://github.com/{ mentor['github'] }.png">
            <div style="flex-grow:1;margin-left:20px;" >
                <a href="https://github.com/{ mentor['github'] }">
                    <div>
                    { mentor['name'] }
                    </div>
                </a>
                <div>
                    {mentor['description']}
                </div>
                <div style="margin-top:20px;">
                    Courses
                    <ul>
                        {''.join([f'<a href="{site}/{ course }/"><li>{ course }</li></a>' for course in mentor['courses']]) }
                    </ul>
                </div>
            </div>
        </div>
        """.strip()
