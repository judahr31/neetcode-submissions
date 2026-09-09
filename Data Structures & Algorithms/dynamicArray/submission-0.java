class DynamicArray {
    private int[] array;
    private int size;

    public DynamicArray(int capacity) {
        this.array = new int[capacity];
        this.size = 0;
    }

    public int get(int i) {
        return this.array[i];
    }

    public void set(int i, int n) {
        this.array[i] = n;
    }

    public void pushback(int n) {
        if (size == array.length) {
            resize();
        }

        array[size] = n;
        size++;
    }

    public int popback() {
        size--;
        return array[size];
    }

    private void resize() {
        this.array = Arrays.copyOf(this.array, this.array.length*2);
    }

    public int getSize() {
        return this.size;  
    }

    public int getCapacity() {
        return this.array.length;
    }
}
