from django.test import TestCase
from django.urls import reverse
from .models import Person, Link, Label

class PersonModelTest(TestCase):
    def setUp(self):
        self.label = Label.objects.create(name="Test Label")
        self.person = Person.objects.create(name="John Doe", image=None)
        self.link = Link.objects.create(person=self.person, url="https://example.com", description="Example Link")
        self.person.labels.add(self.label)

    def test_person_creation(self):
        self.assertEqual(self.person.name, "John Doe")
        self.assertEqual(self.person.links.count(), 1)
        self.assertEqual(self.person.labels.count(), 1)

    def test_label_association(self):
        self.assertIn(self.label, self.person.labels.all())

    def test_link_association(self):
        self.assertIn(self.link, self.person.links.all())
        self.assertEqual(self.link.url, "https://example.com")
        self.assertEqual(self.link.description, "Example Link")

class PersonViewTest(TestCase):
    def setUp(self):
        self.label = Label.objects.create(name="Test Label")
        self.person = Person.objects.create(name="Jane Doe", image=None)
        self.person.labels.add(self.label)

    def test_person_list_view(self):
        response = self.client.get(reverse('person_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Jane Doe")
        self.assertTemplateUsed(response, 'person_list.html')

    def test_person_detail_view(self):
        response = self.client.get(reverse('person_detail', args=[self.person.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Jane Doe")
        self.assertTemplateUsed(response, 'person_detail.html')

    def test_person_add_view(self):
        response = self.client.get(reverse('person_add'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'person_form.html')

    def test_person_edit_view(self):
        response = self.client.get(reverse('person_edit', args=[self.person.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'person_form.html')

class LabelViewTest(TestCase):
    def setUp(self):
        self.label = Label.objects.create(name="Sample Label")

    def test_label_list_view(self):
        response = self.client.get(reverse('label_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Sample Label")
        self.assertTemplateUsed(response, 'label_list.html')

    def test_label_detail_view(self):
        response = self.client.get(reverse('label_detail', args=[self.label.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Sample Label")
        self.assertTemplateUsed(response, 'label_detail.html')

class LinkModelTest(TestCase):
    def setUp(self):
        self.person = Person.objects.create(name="John Doe", image=None)
        self.link = Link.objects.create(person=self.person, url="https://example.com", description="Example Link")

    def test_link_creation(self):
        self.assertEqual(self.link.person, self.person)
        self.assertEqual(self.link.url, "https://example.com")
        self.assertEqual(self.link.description, "Example Link")
