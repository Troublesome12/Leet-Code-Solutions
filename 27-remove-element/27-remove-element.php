class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $val
     * @return Integer
     */
    
    function removeKeys(&$nums, $val) {
        $key = array_search($val, $nums);
        if (false !== $key) {
            unset($nums[$key]);
            $this->removeKeys($nums, $val);
        }
    }
    
    function removeElement(&$nums, $val) {
        $this->removeKeys($nums, $val);
    }
}