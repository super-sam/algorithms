public class LinkedOfStackStrings {
    Node top = null;
    class Node{
        String info;
        Node next;
    }

    public boolean isEmpty(){
        return top == null;
    }

    public String peek(){
        String item = null;
        if (!isEmpty()){
            item = top.info;
        }
        return item;
    }

    public String pop(){
        String item = peek();
        if (!isEmpty()){
            top = top.next;
        }
        return item;
    }

    public void push(String info){
        Node node = new Node();
        node.info = info;
        node.next = top;
        top = node;
    }
    public static void main(String[] args){
        LinkedOfStackStrings linkedList = new LinkedOfStackStrings();
        linkedList.push("1");
        linkedList.push("2");
        linkedList.push("3");
        System.out.println(linkedList.isEmpty());
        System.out.println(linkedList.pop());
        System.out.println(linkedList.pop());
        System.out.println(linkedList.pop());
        System.out.println(linkedList.isEmpty());
        System.out.println(linkedList.pop());
    }
}
