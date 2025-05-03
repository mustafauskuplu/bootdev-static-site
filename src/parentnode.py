from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("Tag is mandatory for a parent node.")
        
        if not self.children:
            raise ValueError("Children is mandatory for a parent node.")
        
        return f"<{self.tag}>{self.__children_html__(self.children)}</{self.tag}>"
    
    def __children_html__(self, children, html_so_far = ""):

        for child in children:
            html_so_far += child.to_html()
            
            # if isinstance(child, ParentNode):
            #     html_so_far += child.__parent_html__(html_so_far)
            # else:
            #     html_so_far += child.to_html()

        return html_so_far


            




        
