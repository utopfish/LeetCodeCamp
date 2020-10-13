package middle;

public class c0529updateBoard {
    int [] disx={-1,0,1,-1,1,-1,0,1};
    int [] disy={-1,-1,-1,0,0,1,1,1};
    public char[][] updateBoard(char[][] board, int[] click) {
        int x=click[0];
        int y=click[1];
        if (board[x][y]=='M'){
            board[x][y]='X';
        }
        else{
            inboard(board,x,y);
        }
        return board;
    }
    public  void inboard(char[][] board,int x,int y){
        int count=0;
        for (int i=0;i<8;i++){
            int new_x=x+disx[i];
            int new_y=y+disy[i];
            if (new_x <0 || new_x >= board.length || new_y < 0|| new_y >=board[0].length){
                continue;
            }
            else if (board[new_x][new_y]=='M'){
                count++;
            }
        }
        if (count!=0){
            board[x][y]=(char) (count + '0');
        }else{
            board[x][y]='B';
            for (int i=0;i<8;i++){
                int new_x=x+disx[i];
                int new_y=y+disy[i];
                if (new_x < 0 || new_x >= board.length || new_y < 0|| new_y >=board[0].length || board[new_x][new_y]!='E'){
                    continue;
                }
                inboard(board,new_x,new_y);
            }
        }
    }
}
