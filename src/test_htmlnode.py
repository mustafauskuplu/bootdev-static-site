import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    
    def test_repr(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        node = HTMLNode("a", "This is a link.", None, props)
        self.assertEqual(f"{node}", f"HTMLNode(tag: a, value: This is a link., children: None, props: {props})")

    def test_to_html(self):
        node = HTMLNode()
        self.assertRaises(NotImplementedError, node.to_html)

    def test_props_to_html(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        node = HTMLNode(None, None, None, props)
        self.assertEqual(' href="https://www.google.com" target="_blank"', node.props_to_html())


if __name__ == "__main__":
    unittest.main()