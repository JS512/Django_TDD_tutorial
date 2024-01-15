from django.test import TestCase

from .models import Task

# Create your tests here.
class TaskModelTest(TestCase) :
    def test_task_model_exists(self) :
        tasks = Task.objects.count()

        self.assertEqual(tasks, 0)

    def test_model_has_string_representation(self) :
        task = Task.objects.create(title='First task')

        self.assertEqual(str(task), task.title)

class IndexPageTest(TestCase) :
    def setUp(self) :
        self.task = Task.objects.create(title='First task')

    def test_index_page_returns_correct_response(self) :
        response = self.client.get('/')

        self.assertTemplateUsed(response, 'task/index.html')
        self.assertEqual(response.status_code, 200)
    
    def test_index_page_has_tasks(self) :
        

        response = self.client.get('/')

        self.assertContains(response, self.task.title)


class DetailPageTest(TestCase) :
    def setUp(self) :
        self.task = Task.objects.create(title='First task', description="The description")
        self.task2 = Task.objects.create(title='Second task', description="The description")
    
    def test_detail_page_returns_correct_response(self) :
        response = self.client.get(f'/{self.task.id}/')

        self.assertTemplateUsed(response, 'task/detail.html')
        self.assertEqual(response.status_code, 200)


    def test_detail_page_has_correct_response(self) :
        response = self.client.get(f'/{self.task.id}/')

        self.assertContains(response, self.task.title)
        self.assertContains(response, self.task.description)
        self.assertNotContains(response, self.task2.title)


class NewPageTest(TestCase) :
    def test_new_page_returns_correct_response(self) :
        response = self.client.get('/new/')

        self.assertTemplateUsed(response, 'task/new.html')
        self.assertEqual(response.status_code, 200)