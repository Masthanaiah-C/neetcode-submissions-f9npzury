/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
        if (head == nullptr) return head;
        std::map <Node*, Node*> v;
        v[nullptr] = nullptr;
        Node* saveHead = head;
        while (head != nullptr) {
            v[head]= new Node(head->val);
            head = head ->next;
        }

        for (const auto& [key, value] : v) {
            if(key == nullptr) continue;
            value->val = key->val;
            value->next = v[key->next];
            value->random = v[key->random];
        }
        return v[saveHead];
    }
};
