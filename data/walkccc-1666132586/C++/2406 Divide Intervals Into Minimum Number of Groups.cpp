class Solution {
 public:
  // Very simliar to 253. Meeting Rooms II
  int minGroups(vector<vector<int>>& intervals) {
    // Store `right`s
    priority_queue<int, vector<int>, greater<>> minHeap;

    sort(begin(intervals), end(intervals));

    for (const vector<int>& interval : intervals) {
      if (!minHeap.empty() && interval[0] > minHeap.top())
        minHeap.pop();  // No overlap, we can reuse the same group
      minHeap.push(interval[1]);
    }

    return minHeap.size();
  }
};