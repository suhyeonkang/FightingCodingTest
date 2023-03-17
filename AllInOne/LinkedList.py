class LinkedListNode(object) :
    def __init__(self, val = 0, next = None, prev = None) :
        self.next = next
        self.prev = prev
        self.val = val

class BrowserHistory:

    ## 최초 노드를 만드는 함수 
    def __init__(self, homepage: str):
        
        self.head = self.current = LinkedListNode(val=homepage)


    ##  페이지 앞의 기록은 삭제되고 url로 방문함
    def visit(self, url: str):
        self.current.next = LinkedListNode(val=url, prev=self.current)
        self.current = self.current.next
        return None
        

    ## steps 수 만큼 뒤로 가기를 하고 url return(뒤로 가기를 할 수 있는 page 수 안에서 )
    def back(self, steps: int) :

        while steps > 0 :
            self.current = self.prev
            steps -= 1
            if(self.current == self.head):
                break
            
        return self.val
        

    ## steps 수 만큼 앞으로 가기를 하고 url return  (앞으로 가기를 할 수 있는 page 수 안에서)
    def forward(self, steps: int) :

        while steps > 0 :
            self.current = self.next
            steps -= 1
            if(self.current.next == ''):
                break
        return self.val    