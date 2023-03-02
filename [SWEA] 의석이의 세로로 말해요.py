'''
 - 5개의 단어 중 가장 긴 단어를 기준으로 한다
 - 가장 긴 길이보다 짧은 단어가 있다면 공백으로 채워준다
 - 열을 순회하면서 단어를 이어주되, 문장 속 공백 제거하며 출력

 => 다른 풀이를 찾아보니 try, except를 이용하는 방법을 알게되었다.
    try, except는 인덱스 에러 나지 않도록 해줌!
    try:
        실행할 코드
    except:
        예외가 발생했을 때 처리하는 코드
'''
T = int(input())
for tc in range(1,T+1):
    words = []  # 다섯 단어를 담을 리스트
    say = ''    # 출력할 결과 변수

    for _ in range(5):
        word = input()
        words.append(word)


    for i in range(15): # 문자열 길이는 15이하이므로
        for j in range(5):
            # try, except는 인덱스 에러 제거
            try:
                say += words[j][i]
            except:
                continue

    print(f'#{tc} {say}')

    # [내가 풀었던 방법]
    # T = int(input())
    # for tc in range(1, T + 1):
    #     size = 0
    #     words = []
    #     say = ''
    #
    #     for _ in range(5):
    #         word = input()
    #         words.append(word)
    #         if len(word) > size:
    #             size = len(word)
    #
    #     for i in range(size):
    #         for j in range(5):
    #             if len(words[j]) < size:
    #                 words[j] += ' '
    #             say += words[j][i]
    #
    #     say = say.replace(' ', '')
    #     print(f'#{tc} {say}')