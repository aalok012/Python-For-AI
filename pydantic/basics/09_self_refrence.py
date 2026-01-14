from typing import List, Optional
from pydantic import BaseModel


class Comment(BaseModel):
    id: int
    content: str
    replies: Optional[List['Comment']]= None
    
Comment.model_rebuild()

comment= Comment(
    id=100,
    content="First video",
    replies=[Comment(id=2, content="reply1"),
                     Comment(id=7, content="reply2"),
                                     Comment(id=4, content="reply3", replies=[Comment(id=5, content="reply3.1")])]
)
print(comment)