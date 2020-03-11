#!/usr/bin/env python
text = {
    'home': {
        'name': 'Li',
        'occupation': 'Founder',
        'career': 'Entrepreneur',
        'rank': 'Senior Airman',
        'company': 'ESFE'
    },
    'about': {
        'greet': 'Hi, I am Li Dai, a veteran, software engineer, and technology enthusiast. ',
        'first_paragraph': '',
        'second_paragraph': ''
    },
    'services': {
        'service_1': 'Leadership',
        'service_2': 'Curiosity',
        'service_3': 'Adaptability',
        'service_4': 'Innovation',
        'purpose': 'My Motto: ',
        'content': 'The importance of luck to our success diminishes as time goes longer.  It is a simple probability '
                   'problem! '
    },
    'expertise': {
        'exp_1': {
            'name': 'Leadership',
            'content': 'Success of one\'s self isn\'t a true leader.  I strive for everyone\'s success around me'
        },
        'exp_2': {
            'name': 'Product Management',
            'content': 'I spend my weekends to guide a group of motivated individuals to create meaningful products'
        },
        'exp_3': {
            'name': 'Software Development',
            'content': 'Building software including mobile and web to make the world a better place!'
        },
        'exp_4': {
            'name': 'Agile Development',
            'content': 'Following agile principles daily to develop reliable and useful products in shortest time '
                       'possbile '
        },
        'exp_5': {
            'name': 'Innovation',
            'content': 'Curiosity to do things differently is always in me.  It leads directly to innovative ideas '
                       'and creativity '
        },
        'exp_6': {
            'name': 'Lean Development',
            'content': 'I exercise lean principles both in work and life. Minimize costs and build MVP\'s ASAP'
        }

    },
    'metrics': {
        'metric_1': {
            'name': 'Cities',
            'value': '30'
        },
        'metric_2': {
            'name': 'Countries',
            'value': '6'
        },
        'metric_3': {
            'name': 'Languages',
            'value': '4'
        },
        'metric_4': {
            'name': 'Careers',
            'value': '2'
        }

    },
    'skills': {
        'skill_1': {
            'name': 'Java',
        },
        'skill_2': {
            'name': 'Jira',
        },
        'skill_3': {
            'name': 'Python',
        },
        'skill_4': {
            'name': 'SQL',
        },
        'skill_5': {
            'name': 'AWS',
        },
        'skill_6': {
            'name': 'Confluence',
        }

    },
    'education': {
        'degree_1': {
            'degree_name': 'Master of Arts in Computer Science',
            'story': 'When transitioned to my new career as a Queens College student, \
							I participated in various club activities and volunteer work. \
							Some interesting ones include Treasurer of Veteran\'s Club, \
							Proctor for ACM Algorithm Competition, and Teaching Assistant for C++\
							',
            'courses': [
                'Advanced OOP in Java & C++',
                'Theory of Quantum Computing',
                'Time & Space Complexity',
                'Image Processing & Computer Graphics',
                'Database Systems',
                'Operating Systems & Distributed Systems',
                'Machine Learning in Finance ',
                'Algorithms & Data Structures'
            ]
        },

        'degree_2': {
            'degree_name': 'Bachelor of Arts in Applied Mathematics & Psychology',
            'story': 'Believed in Mathematics is human\'s way of understanding the universe, \
							and Psychology is our way to understand human, I relentlessly pursued a double degree \
							in these two in hope they will help me both the world and people better\
							',
            'courses': [
                'Advanced Calculus',
                'Differential Equation',
                'Mathematics Problem Solving',
                'Probability & Statistics',
                'Linear Algebra',
                'Advanced Experimental Psychology',
                'Psychometrics',
                'Industrial & Organizational Psychology'
            ]
        },

    },
    'direction': ['Left', 'Top', 'Right', 'Bottom'],

    'works': [
        {
            'title_company': 'Founder/Tech Lead at ESFE',
            'time_range': 'July 2019 - Present',
            'content': [
                'Recruited 20 people to voluntarily work ESFE projects',
                'Set up infrastructures on AWS for app development',
                'Set up Trello/JIRA board to follow agile development',
                'Designed app architecture including mobile, server, and database',
                'Conducted scrum meetings, wrote product roadmaps, and set deadlines',
                'Interviewed potential clients about feedbacks and product features',
                'Implemented and hosted static s3 websites using HTML / CSS',
                'https://nycesfe.com/'
            ]
        },
        {
            'title_company': 'Data Platform Engineer at White Ops',
            'time_range': 'Feb 2019 - Present',
            'content': [
                'Built and maintained platforms that process 1 billion messages per day',
                'Developed integration tests for multiple applications in docker containers',
                'Implemented decompression and compression to reduce throughput by 80%',
                'Tested applications on AWS in linux system with tools rabbitMQ, Kafka, and Locust',
                'Implemented metric and health system in existing applications',
                'Customized and rewrote Kafka producer to better fit team needs',
                'Weekly deployment of application using CI process on gitlab',
                'Implemented application dead letter queues sending to AWS S3'
            ]
        },
        {
            'title_company': 'Software Engineer at Fidelity Investments',
            'time_range': 'Jan 2018 - Feb 2019',
            'content': [
                'Responsible for Adobe Analytics migration to AWS',
                'Refactored E-mail templates to utlize functions of Apache Velocity template engine'
                'Re-designing and developing existing Spring Batch process to prevent process failures',
                'Acted as release captain to coordinate and perform scheduled software releases',
                'Maintaining and monitoring existing linux servers and file systems',
                'Designed and implemented algorithm for group level Hackathon',
                'Decommissioning and cleaning up unused codes',
                'Manipulating meta data on Oracle database to test existing batch process',
                'Obtained AWS certification 2 months after knowing our team\'s cloud movement'
            ]
        },
        {
            'title_company': 'Software Engineer Intern at Lift Rocket',
            'time_range': 'Feb 2017 - Apr 2017',
            'content': [
                'Designed and developed transactional and analytical data structures',
                'Modified existing software to correct Facebook login issue and improve performance',
                'Worked closely with other team members to plan, design and develop robust solutions',
                'Advocated for a hackathon to boost work progress by roughly 2 weeks',
                'Wrote sql queries to support website function'
            ]
        },
        {
            'title_company': 'Software Engineer Intern at Hooch Inc.',
            'time_range': 'Jan 2016 - May 2016',
            'content': [
                'Self taught Ruby and Javascript to develop mobile applications in a fast pace startup environment',
                'Integrated Company App with Amazon Echo by making a Alexa Skill using AWS, Javascript, and Python',
                'Created a Hubot to improve communication between sales and technical team',
                'Maintained backend database and servers using Ruby on Rails and AWS',
                'Developed an automated email generating program using Ruby with gem SMTP',
                'Fixed image error on Website within 2 weeks from not knowing WordPress to a problem solver'
            ]
        },
        {
            'title_company': 'Aviation Electronics Specialist',
            'time_range': 'Oct 2010 - Oct 2014',
            'content': [
                'Performed general maintenance on A10 aircrafts to ensure aircraft was mission capable',
                'Organized government properties daily to keep track of aircraft maintenance record',
                'Step promoted 6 month ahead to E-4. Top scorer for E-5 promotion',
                'Supervised and trained DM Air Force Base Honor Guard to perform funerals, \
				 change of commands, and color guard duties as a lead trainer',
                'Maintained extreme professionalism and led by example',
                'Managed and led approximated 150 airmen trainees as an airman leader at Sheppard Air Force base. \
				 Squadron duties include: drills, duty scheduling, and safety training',
                'Airman of the Quarter 2012 Spring, Distinguished Technical Training Graduate 2011, BMT Honor Graduate 2010',
                'Obtained secret clearance'
            ]
        },

    ],
    'projects': {

    },
    'blog': {

    },
    'contact': {

    }

}
