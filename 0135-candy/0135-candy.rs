use std::cmp::Reverse;
use std::collections::BinaryHeap;

impl Solution {
    pub fn candy(ratings: Vec<i32>) -> i32 {
        let n = ratings.len();
        // BinaryHeap is a max-heap, so wrap in Reverse for a min-heap
        let mut heap: BinaryHeap<Reverse<(i32, usize)>> = ratings
            .iter()
            .enumerate()
            .map(|(i, &r)| Reverse((r, i)))
            .collect();
        let mut candies = vec![0; n];

        while let Some(Reverse((rating, i))) = heap.pop() {
            let mut c = 1;
            if i > 0 && rating > ratings[i - 1] {
                c = c.max(candies[i - 1] + 1);
            }
            if i + 1 < n && rating > ratings[i + 1] {
                c = c.max(candies[i + 1] + 1);
            }
            candies[i] = c;
        }

        candies.iter().sum()
    }
}