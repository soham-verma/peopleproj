# Adding and Editing People

    Add a Person:
    Go to http://127.0.0.1:8000/people/add/ to add a new person, upload an image, assign labels, and add link URLs.

    Edit a Person:
    Visit a person’s detail page (e.g., /people/1/) and click "Edit". Update their information and associated links.

    Delete a Person:
    From the person’s detail page, click "Delete" to remove them from the database.

# Managing Labels

    List All Labels:
    http://127.0.0.1:8000/labels/ displays all labels.

    View Label Details:
    Clicking on a label shows all people associated with it.

    Add/Edit Labels via Admin:
    Use the Django admin at /admin/ to manage labels. You can also integrate label creation forms in the frontend if needed.

# Filtering and Searching

    Filter by Label: Append ?label=<label_id> to the People list URL, e.g., /people/?label=2.

    Search by Name: Append ?q=<search_term> to the People list URL, e.g., /people/?q=John.