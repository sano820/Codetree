import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // 문제에서 주어진 5개의 문자열을 배열에 저장
        String[] arr = {"apple", "banana", "grape", "blueberry", "orange"};

        // 영문자 하나 입력받기
        char ch = sc.next().charAt(0);

        // 조건에 맞는 문자열의 개수를 저장할 변수
        int count = 0;

        // 배열에 있는 문자열을 하나씩 확인
        for (int i = 0; i < arr.length; i++) {

            // Java 인덱스는 0부터 시작하므로
            // 세 번째 문자는 charAt(2), 네 번째 문자는 charAt(3)
            if (arr[i].charAt(2) == ch || arr[i].charAt(3) == ch) {

                // 조건에 맞는 문자열 출력
                System.out.println(arr[i]);

                // 조건에 맞는 문자열 개수 증가
                count++;
            }
        }

        // 마지막에 조건에 맞는 문자열의 총 개수 출력
        System.out.println(count);
    }
}