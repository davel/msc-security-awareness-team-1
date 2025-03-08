# Integrating Wazuh and OpenVAS

Our assignment required "Integration of Wazuh with OpenVAS for unified
reporting".

Much searching online finds that some people have asked about doing this,
however there is no sign in the documentation of both tools they it is a
existing feature.

Curiously We found a
[blog article](https://www.infopercept.com/blogs/supercharge-your-security-integrate-openvas-with-wazuh-for-comprehensive-vulnerability-scanning-and-threat-detection)
which describes integrating the two using the "OpenVAS plugin for Wazuh".
This does not seem to exist, at least not in the Wazuh source code. The writing
style suggests to me that the article was written with generative AI.

We found that ChatGPT will also hallucinate a method to integrate the two, but
this time give non-existent configuration parameters for Greenbone.

Was the requirement a hallucination itself?

# A practical approach

Integration is certainly possible. The respective API provide a means for
[pulling data from Greenbone](https://greenbone.github.io/python-gvm/api/gmpv225.html#gvm.protocols.gmp.GMPv225.get_reports)
and
[injecting it in to Wazuh](https://documentation.wazuh.com/current/user-manual/api/reference.html#operation/api.controllers.event_controller.forward_event)

We later found some
[software which claims to do this](https://github.com/MuhamadAjiW/Gvm-Scripts)
although we did not try it for reasons of time.
