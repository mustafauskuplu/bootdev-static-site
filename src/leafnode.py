from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if not self.value:
            raise ValueError
        
        if not self.tag:
            return self.value
        
        if self.tag == "img":
            alt = self.props.get("alt", self.value)
            return f'<img{self.props_to_html()} alt="{alt}" />'
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"