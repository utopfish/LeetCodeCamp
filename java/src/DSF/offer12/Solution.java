package DSF.offer12;

class Solution {
    public int[][] visited;
    public boolean hasNext(char[][] board,String word,int count,int len,int x,int y){
        int temp[][]={{0,-1},{0,1},{1,0},{-1,0}};
        if (count==len){
            return true;
        }else{
            for (int i =0;i<4;i++){
                int new_x=x+temp[i][0];
                int new_y=y+temp[i][1];
                if (-1<new_x && new_x<visited.length && -1<new_y && new_y<visited[0].length && visited[new_x][new_y]==0){
                    if (board[new_x][new_y]==word.charAt(count)){
                        visited[new_x][new_y]=1;
                        if (hasNext(board,word,count+1,len,new_x,new_y)){
                            return true;
                        }
                        visited[new_x][new_y]=0;
                    }
                }
            }
            return false;
        }
    }
    public boolean exist(char[][] board, String word) {
        visited=new int[board.length][board[0].length];
        int len=word.toCharArray().length;
        int count=0;
        for (int i=0;i<board.length;i++){
            for (int j=0;j<board[i].length;j++){
                if (word.charAt(count)==board[i][j]){
                    visited[i][j]=1;
                    if (hasNext(board,word,count+1,len,i,j)){
                        return true;
                    }
                }
            }
        }
        return false;
    }
    public static void main(String[] args){
        char[][] board={
                {'A','B','C','E'},
                {'S','F','C','S'},
                {'A','D','E','E'}};
        String s="ABCCED";
        Solution solution=new Solution();
        System.out.println(solution.exist(board,s));
    }
}
