{
    'name': 'Project-Notes Integration',
    'version': '1.0',
    'summary': 'Enhance Collaboration and Task Management with Advanced Projects-Notes Integration',
    'sequence': 10,
    'description': """
        Project-Notes Integration
        =========================
        This module seamlessly integrates the Projects module with the Notes module in Odoo, enabling a more streamlined and efficient management of notes within project workflows. It enhances collaboration among team members by providing an easy way to link notes to specific projects and tasks, ensuring that all relevant information is easily accessible and organized.

        Key Features:
        -------------
        * Link notes directly to projects and tasks.
        * Easily manage and access notes from the project dashboard.
        * Enhance collaboration and information sharing among team members.
        * Keep all project-related notes organized and easily accessible.

        This module is ideal for teams looking to improve their project management processes and ensure that all important notes and information are closely tied to their relevant projects and tasks.
        """,
    'category': 'Project Management',
    'website': 'https://proyectasoft.odoo.com',
    # 'images': ['static/description/banner.png'],  # Ensure you have a banner.png in static/description.
    'depends': ['project', 'note'],
    'data': [
        'views/note_view.xml',
        'views/project_view.xml',
        'views/project_task_view.xml',
    ],
    'demo': ['data/demo.xml'],  # Include demo data if available
    'installable': True,
    'application': True,
    'auto_install': False,
    'author': 'Felipe Ferreira',
    'license': 'AGPL-3',
    'price': 0.00,  # Include a price if applicable
    'currency': 'USD',  # Include currency if you set a price
}
