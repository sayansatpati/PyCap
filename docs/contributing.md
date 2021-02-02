# Contributing

## Our Mentors

{% for mentor in mentors %}
<div id="mentor-{{ mentor['github'] }}" style="display: flex;margin-bottom:30px;">
    <img style="border-radius:50%;width:80px;height:80px" src="https://github.com/{{ mentor['github'] }}.png">
    <div style="flex-grow:1;margin-left:20px;" >
      <a href="https://github.com/{{ mentor['github'] }}"><div>
      {{ mentor['name'] }}
      </div></a>
      <div>
      {{mentor['description']}}
      </div>
      <div style="margin-top:20px;">
      Courses
      <ul>
      {% for course in mentor['courses'] %}
        <a href="{{ config.site_url | reverse | replace('/', '', 1) | reverse }}/{{ course }}/"><li>{{ course }}</li></a>
      {% endfor %}
      </ul>
      </div>
    </div>
</div>

{% endfor %}

## Becoming a Mentor