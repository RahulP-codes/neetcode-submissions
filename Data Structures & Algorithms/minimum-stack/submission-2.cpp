class MinStack {
private:
    long min;
    stack<long> st;
public:
    MinStack() {}
    
    void push(int val) {
        if (st.empty()) {
            st.push(0);
            min = val;
        } else {
            st.push(val-min);
            if (val<min) min = val;
        }
    }
    
    void pop() {
        if (st.empty()) return;

        long top = st.top();

        if (top<0) min = min - top;

        st.pop();
    }
    
    int top() {
        long top = st.top();
        return (top>0) ? (top+min) : (int)min;
    }
    
    int getMin() {
        return (int)min;
    }
};
