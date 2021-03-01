# Certified Members

{% for cert_name, students in certifications.items() %}
## {{cert_name}}

{% for student in students %}
{{certified(student)}}
{% endfor %}

{% endfor %}