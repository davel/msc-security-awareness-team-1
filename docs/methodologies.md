# General Methodology

During this project, we used an agile methodology to ensure flexibility in our tasks and operations so that we can get the best result possible when we combine our different parts of work.  
Agile methodology is an iterative approach to projects where tasks are broken down into smaller pieces and made into individual tasks of their own. This is advantageous for a team as the view on the project each week can take shape depending on progress and tasks at hand.  

To succeed using this method, we had to communicate with each other both using GitHub and WhatsApp. Through GitHub, we were able to commit our progress for all team members to access. Weekly meetings were held to review progress on our tasks and envision which tasks should be completed next, giving everyone an insight into what percentage of the project had been finished. This allowed for us to make improvements for the near future on tasks at hand, so that we could make improvements before starting the next set of tasks. We also had a group chat where we were able to give each other updates on what tasks were in progress, so that we could effectively communicate on tasks at hand.

By using Agile methodology for project management and implementing a risk-based approach to security, we ensured that the was efficient and secure. The collaboration between the team, constant communication, and continuous feedback throughout the project allowed us to complete the integration successfully while managing risks effectively. This approach not only enhanced the system’s vulnerability detection capabilities but also contributed to the overall security posture of the environment.


---

# Risk Scoring Methodology

Risk scoring is an important method to know the risks within a project and how dangerous they are. For our methodology, we used a scale as follows:

- **Low severity** - At low risk (rule 0-6)
- **Medium severity** - At moderate risk (rule 7-11)
- **High severity** - At high risk (rule 12-14)
- **Critical severity** - Critical components at risk (rule 15 and higher)

More details for the risk methodology method above are in our breakdown of the Wazuh rule classification.

---

# Technical Product Life Cycle Methodology

## 1. Conceptualization & Planning

At the start of the product lifecycle, the focus was on understanding the requirements and planning the integration of OpenVAS with Wazuh. This stage includes:

- **Identifying Needs**: In this phase, we identified the need for integrating OpenVAS with Wazuh to provide enhanced vulnerability management and security monitoring. The goal was to be able to automate the detection of vulnerabilities and categorize them.
- **Defining Scope**: We outlined the objectives, such as improving vulnerability visibility, making reporting easier, and automating detection of vulnerabilities.
- **Choosing Tools & Technologies**: OpenVAS was chosen for vulnerability scanning, and Wazuh for log analysis and security monitoring. The compatibility of these tools was taken into consideration at this point.
- **Risk Assessment & Mitigation Planning**: We performed an initial risk analysis to identify any challenges or risks in advance; this is the step that we depended on in order to know what to expect and avoid.

---

## 2. Design & Architecture

When the first stage was done, we were able to move onto the technical evaluation of the design and architecture. 

- **System Architecture**: We designed the architecture to ensure that OpenVAS and Wazuh could work together efficiently. These were incorporated into virtual machines.
- **Data Flow Mapping**: The data transfer from OpenVAS to Wazuh was defined.
- **Integration Design**: The configurations and blueprints were planned out for how the integrations would work between Wazuh and OpenVAS.

---

## 3. Development & Configuration

This is where the coding and configuration took place.

- **OpenVAS Setup**: OpenVAS was configured to carry out scans of potential vulnerabilities. This was implemented onto a machine.
- **Wazuh Setup & Customization**: We set up Wazuh for monitoring and processing security concerns. This was also set up on a machine.
- **Python Setup**: A Python code was created to generate logs and attacks against the server and player activities.
- **Testing**: During the development phase, we performed continuous testing of the deployment of our project, modifying our aims as we went.

---

## 4. Deployment

Once development and configuration were complete, the deployment phase involved releasing the integrated system into a live server.

- **System Deployment**: The integrated OpenVAS and Wazuh solution was deployed into a live environment.
- **Documentation**: Documentation was created to detail the deployment process, integrations, and issues that were mitigated.

---

## 5. Monitoring & Maintenance

After deployment, monitoring and maintenance were essential to ensure the components worked with each other.

- **Continuous Monitoring**: OpenVAS and Wazuh were monitored to ensure that they were scanning and displaying issues.
- **Updates & Patching**: The software was kept up to date to ensure compatibility.
- **Feedback Loop**: Regular feedback from the team and stakeholders made it so that future goals for improvements were clear and could be made where possible.

---

