import json
from django.test import TestCase, Client
from django.urls import reverse


class SaathiAIAgentTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_saathi_chat_general(self):
        response = self.client.post(
            reverse("saathi_chat_api"),
            data=json.dumps({"query": "Hello Saathi", "action": "general"}),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data.get("success"))
        self.assertIn("reply", data)
        self.assertTrue(len(data["reply"]) > 0)

    def test_saathi_tell_story(self):
        response = self.client.post(
            reverse("saathi_chat_api"),
            data=json.dumps({
                "query": "I am a potter from Bankura making terracotta horses",
                "action": "tell_story"
            }),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data.get("success"))
        self.assertIn("reply", data)

    def test_saathi_price_work(self):
        response = self.client.post(
            reverse("saathi_chat_api"),
            data=json.dumps({
                "query": "How much should I price my Channapatna toy set?",
                "action": "price_work"
            }),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data.get("success"))
        self.assertIn("reply", data)

    def test_saathi_show_work(self):
        response = self.client.post(
            reverse("saathi_chat_api"),
            data=json.dumps({
                "query": "How to photograph metal craft?",
                "action": "show_work"
            }),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data.get("success"))
        self.assertIn("reply", data)

    def test_saathi_find_buyers(self):
        response = self.client.post(
            reverse("saathi_chat_api"),
            data=json.dumps({
                "query": "Where can I find buyers for Banarasi silk?",
                "action": "find_buyers"
            }),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data.get("success"))
        self.assertIn("reply", data)

    def test_saathi_catalog_api(self):
        response = self.client.post(
            reverse("saathi_catalog_api"),
            data=json.dumps({
                "transcript": "Handmade red clay pot with floral engravings, 12 hours of wheel crafting."
            }),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data.get("success"))
        self.assertIn("name", data)
        self.assertIn("category", data)
