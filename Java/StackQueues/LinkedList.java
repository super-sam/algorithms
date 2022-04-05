public class LinkedList<Item> {
    Node top = null;
    class Node{
        Item info;
        Node next;
    }

    public boolean isEmpty(){
        return top == null;
    }

    public Item peek(){
        Item info = null;
        if (!isEmpty()){
            info = top.info;
        }
        return info;
    }

    public Item pop(){
        Item info = peek();
        if (!isEmpty()){
            top = top.next;
        }
        return info;
    }

    public void push(Item info){
        Node node = new Node();
        node.info = info;
        node.next = top;
        top = node;
    }

    public static void main(String[] args){
        LinkedList<String> linkedList = new LinkedList<String>();
        linkedList.push("1");
        linkedList.push("2");
        linkedList.push("3");
        System.out.println(linkedList.isEmpty());
        System.out.println(linkedList.pop());
        System.out.println(linkedList.pop());
        System.out.println(linkedList.pop());
        System.out.println(linkedList.isEmpty());
        System.out.println(linkedList.pop());

        LinkedList<Integer> linkedListInt = new LinkedList<Integer>();
        linkedListInt.push(1);
        linkedListInt.push(2);
        linkedListInt.push(3);
        System.out.println(linkedListInt.isEmpty());
        System.out.println(linkedListInt.pop());
        System.out.println(linkedListInt.pop());
        System.out.println(linkedListInt.pop());
        System.out.println(linkedListInt.isEmpty());
        System.out.println(linkedListInt.pop());
    }

}
