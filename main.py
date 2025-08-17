<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>토론 수업 사전 읽기 자료</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Inter', sans-serif;
        }
        /* 커스텀 스크롤바 스타일 */
        ::-webkit-scrollbar {
            width: 8px;
        }
        ::-webkit-scrollbar-track {
            background: #f1f1f1;
        }
        ::-webkit-scrollbar-thumb {
            background: #888;
            border-radius: 4px;
        }
        ::-webkit-scrollbar-thumb:hover {
            background: #555;
        }
        .topic-card {
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        .topic-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
        }
    </style>
</head>
<body class="bg-gray-50 text-gray-800">

    <!-- 전체 컨테이너 -->
    <div class="container mx-auto p-4 md:p-8 max-w-7xl">

        <!-- 헤더: 타이틀, 로그인 정보, 포인트 -->
        <header class="bg-white shadow-md rounded-xl p-6 mb-8 flex flex-col md:flex-row justify-between items-center sticky top-4 z-10 backdrop-blur-sm bg-opacity-80">
            <div>
                <h1 class="text-3xl font-bold text-gray-900">AI 시대, 교육의 미래 토론</h1>
                <p class="text-gray-600 mt-1">사전 읽기 자료를 통해 자신의 논지를 세워보세요.</p>
            </div>
            <div id="auth-container" class="mt-4 md:mt-0 text-right w-full md:w-auto">
                <!-- 로그인 폼 또는 사용자 정보가 여기에 동적으로 추가됩니다 -->
            </div>
        </header>

        <!-- 토론 주제 목록 -->
        <main id="topics-container" class="space-y-8">
            <!-- 주제 카드들이 여기에 동적으로 추가됩니다 -->
        </main>

    </div>

    <!-- Firebase SDK 및 초기화 스크립트 -->
    <script type="module">
        // Firebase 모듈 가져오기
        import { initializeApp } from "https://www.gstatic.com/firebasejs/11.6.1/firebase-app.js";
        import { getAuth, signInAnonymously, onAuthStateChanged } from "https://www.gstatic.com/firebasejs/11.6.1/firebase-auth.js";
        import { getFirestore, doc, getDoc, setDoc, onSnapshot } from "https://www.gstatic.com/firebasejs/11.6.1/firebase-firestore.js";

        // --- 데이터 ---
        const topicsData = [
            {
                title: "① AI 과제 제출은 학생의 노력인가?",
                articles: {
                    pro: [
                        { title: "[박남기의 교단춘추] 생성 AI 시대 보고서 부과 및 평가방법", source: "한교닷컴", date: "2024.10.07", url: "https://www.hangyo.com/news/article.html?no=102726", summary: "AI와의 협업이 결과물에 긍정적 기여, 학생의 생각+AI 답변+후기까지 포함하면 노력 인정." },
                        { title: "[교육 현장에서 LLM 기반 AI 에이전트의 활용 가능성]", source: "Korea Science", date: "2025", url: "https://koreascience.kr/article/JAKO202520357602319.pdf", summary: "학생들이 직접 피드백 받고 자기 결과물을 수정·보완하는 과정이 학습 효과와 노력으로 인정." }
                    ],
                    con: [
                        { title: "활용인가, 표절인가…챗GPT로 과제·논문에 시험까지", source: "데일리안", date: "2024.10.22", url: "https://news.nate.com/view/20241022n01634", summary: "일부 대학(연세대 등) AI 답변만 표절한 과제 0점 처리, 이용 막으려 서약서 요구." },
                        { title: "AI 무단 사용 학생들 모두 D학점…적발 이후 대응", source: "연구윤리정보포털", date: "2025.07.09", url: "https://cre.nrf.re.kr/bbs/BoardDetail.do?bbsId=BBSMSTR_000000000179&nttId=15015&pageIndex=1&schBlogId=&searchWrd=&searchCnd=", summary: "AI 대필 과제 적발·불이익 증가, 표절 감지/회피 기술 공존하는 현장 문제점 고발." }
                    ],
                    neutral: [
                        { title: "“AI 안 썼다 증명해야 한다”…'인간 인증' 필요 시대", source: "조선일보", date: "2025.06.10", url: "https://www.chosun.com/economy/weeklybiz/2025/06/19/NOMLP3GB5BCANPZBL2A63YYDPY/", summary: "과제마다 ‘AI 인증’ 논쟁, 인간 인증·비판적 자기 역할 강조. 찬반 양론 함께 소개." },
                        { title: "디지털 교육혁신 현황", source: "데이터 브리프 (NIA)", date: "2024.03", url: "https://www.nia.or.kr/site/nia_kor/ex/bbs/View.do?cbIdx=82618&bcIdx=27527&parentSeq=27527&pageIndex=1&mode=&searchKey=&orderbyDiv=date", summary: "AI 과제 결과물의 맞춤형 효과와 공교육 보완, 문제점까지 중립적으로 분석." }
                    ]
                }
            },
            {
                title: "② 학교의 AI 활용 가이드라인/처벌 필요성",
                articles: {
                    pro: [
                        { title: "“규제는 AI 산업 독?…명확한 가이드라인은 윤활유”", source: "매일경제", date: "2024.06.16", url: "https://www.mk.co.kr/news/it/11061749", summary: "과도한 규제는 피해가 있지만, 명확한 정책과 가이드라인은 오히려 시장 신뢰·공정 확보 도움." },
                        { title: "[AI 기본법 과방위 소위 통과안 주요 내용]", source: "The Codit", date: "2024.11.26", url: "https://thecodit.com/blog/ai-basic-law-updates", summary: "실제 벌칙 및 과태료 등 법률·제도적 처벌 도입 움직임, 입법 현황 분석." }
                    ],
                    con: [
                        { title: "\"2024년은 AI 규제의 해?\" 국내외 AI 법제화 현황", source: "디지털 인사이트", date: "2024.02.15", url: "https://ditoday.com/2024%EB%85%84%EC%9D%80-ai-%EA%B7%9C%EC%A0%9C%EC%9D%98-%ED%95%B4-%EA%B5%AD%EB%82%B4%EC%99%B8-ai-%EB%B2%95%EC%A0%9C%ED%99%94-%ED%98%84%ED%99%99/", summary: "과잉 규제는 산업 성장 억제, 자율적 관리·사회적 합의 중시." },
                        { title: "인공지능 감시에 의한 권력의 확대와 규범적 대응방안 연구", source: "KISDI", date: "2024.10", url: "http://www.kisdi.re.kr/eng/report/e/fileView.do?key=m2102103219640&arrMasterId=4333452&id=1829356", summary: "규제와 처벌은 개인정보 및 국민권리 침해, 투명성·절차 확보 필요." }
                    ],
                    neutral: [
                        { title: "[AI 관련 법제 동향]", source: "법제처", date: "2025.06.14", url: "https://www.moleg.go.kr/boardDownload.es?bid=legnlpst&list_key=3813&seq=1", summary: "규제/자율관리/글로벌 기준 등 다양한 정책 현황과 논쟁 분석." },
                        { title: "[UNESCO 정책 지침서]", source: "UNESCO", date: "2024.06", url: "https://unesco.or.kr/wp-content/uploads/2024/06/%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5%EA%B3%BC-%EA%B5%90%EC%9C%A1-%EC%A0%95%EC%B1%85%EC%9E%85%EC%95%88%EC%9E%90%EB%A5%BC-%EC%9C%84%ED%95%9C-%EC%A7%80%EC%B9%A8.pdf", summary: "가이드라인, 사회적 합의 등 세계적 흐름과 균형 분석." }
                    ]
                }
            },
            {
                title: "③ AI 활용이 학생의 창의성에 미치는 영향",
                articles: {
                    pro: [
                        { title: "AI디지털교과서 도입 찬반논쟁…“맞춤교육”", source: "MS투데이", date: "2024.09", url: "https://www.mstoday.co.kr/news/articleView.html?idxno=93396", summary: "취약점 분석-맞춤형 학습 가능, 미래교육 혁신적 역할 강조." },
                        { title: "디지털 교육혁신 현황", source: "데이터 브리프 (NIA)", date: "2024.03", url: "https://www.nia.or.kr/site/nia_kor/ex/bbs/View.do?cbIdx=82618&bcIdx=27527&parentSeq=27527&pageIndex=1&mode=&searchKey=&orderbyDiv=date", summary: "AI가 맞춤형 교육·공교육 보완 역할, 창의력 증진 기대." }
                    ],
                    con: [
                        { title: "검증 안 된 AI와 교과서의 만남, 학습격차 더 벌어질라", source: "한겨레", date: "2024.10.28", url: "https://www.hani.co.kr/arti/economy/it/1164573.html", summary: "주입식·문제풀이 기능에 치중, 창의력 강화와 거리가 있다는 비판." },
                        { title: "AI디지털교과서 도입 찬반논쟁…“인지발달 저해”", source: "MS투데이", date: "2024.09", url: "https://www.mstoday.co.kr/news/articleView.html?idxno=93396", summary: "디지털 기기 노출 증가, 학습 능력 저하와 인지발달 저해 우려." }
                    ],
                    neutral: [
                        { title: "AI디지털교과서 도입 찬반논쟁", source: "MS투데이", date: "2024.09", url: "https://www.mstoday.co.kr/news/articleView.html?idxno=93396", summary: "찬성/반대 양론, 맞춤교육과 우려, 균형 있게 제시." },
                        { title: "한겨레 및 교원단체 전문가 인터뷰", source: "한겨레", date: "2024.10.28", url: "https://www.hani.co.kr/arti/economy/it/1164573.html", summary: "정부 정책, 전문가·교원 등 다양한 의견·현장 분석." }
                    ]
                }
            }
        ];

        // --- Firebase 설정 ---
        const appId = typeof __app_id !== 'undefined' ? __app_id : 'default-app-id';
        const firebaseConfig = typeof __firebase_config !== 'undefined' ? JSON.parse(__firebase_config) : {};
        
        let app, db, auth;
        let studentInfo = null; // 학번/이름으로 로그인한 정보
        let firebaseUser = null; // 익명 인증 사용자 정보
        let unsubscribeUserPoints = null;

        try {
            app = initializeApp(firebaseConfig);
            db = getFirestore(app);
            auth = getAuth(app);
        } catch (e) {
            console.error("Firebase 초기화 오류:", e);
        }

        // --- UI 렌더링 함수 ---
        const authContainer = document.getElementById('auth-container');
        const topicsContainer = document.getElementById('topics-container');

        // 로그인 상태에 따라 UI 업데이트
        const updateUI = () => {
            if (studentInfo && firebaseUser) {
                // 로그인 상태
                authContainer.innerHTML = `
                    <div class="flex items-center justify-end space-x-4">
                        <div class="text-right">
                           <p class="font-semibold">${studentInfo.name} (${studentInfo.studentId})</p>
                           <p class="text-xs text-gray-500">로그인되었습니다.</p>
                        </div>
                        <div class="text-center">
                            <p class="text-lg font-bold text-indigo-600" id="points-display">0 P</p>
                            <p class="text-xs text-gray-500">읽기 포인트</p>
                        </div>
                        <button id="logout-btn" class="bg-red-500 hover:bg-red-600 text-white font-bold py-2 px-4 rounded-lg transition-colors">로그아웃</button>
                    </div>
                `;
                document.getElementById('logout-btn').addEventListener('click', handleLogout);
                listenToUserPoints(firebaseUser.uid);
            } else {
                // 로그아웃 상태
                if (unsubscribeUserPoints) {
                    unsubscribeUserPoints();
                    unsubscribeUserPoints = null;
                }
                authContainer.innerHTML = `
                    <form id="login-form" class="flex flex-col sm:flex-row items-center justify-end space-y-2 sm:space-y-0 sm:space-x-2">
                        <input type="text" id="student-id" placeholder="학번" class="w-full sm:w-auto px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500" required>
                        <input type="text" id="student-name" placeholder="이름" class="w-full sm:w-auto px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500" required>
                        <button type="submit" class="w-full sm:w-auto bg-indigo-600 hover:bg-indigo-700 text-white font-bold py-2 px-4 rounded-lg transition-colors">로그인</button>
                    </form>
                `;
                document.getElementById('login-form').addEventListener('submit', handleLogin);
            }
        };
        
        // 토론 주제 및 기사 목록 렌더링
        const renderTopics = () => {
            topicsContainer.innerHTML = '';
            topicsData.forEach(topic => {
                const topicEl = document.createElement('div');
                topicEl.className = 'bg-white p-6 rounded-xl shadow-sm topic-card';
                topicEl.innerHTML = `
                    <h2 class="text-2xl font-bold mb-4 border-b pb-3">${topic.title}</h2>
                    <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                        ${createArticleSection('찬성', topic.articles.pro, 'blue')}
                        ${createArticleSection('반대', topic.articles.con, 'red')}
                        ${createArticleSection('중립/분석', topic.articles.neutral, 'green')}
                    </div>
                `;
                topicsContainer.appendChild(topicEl);
            });
            addArticleClickListeners();
        };

        // 찬성/반대/중립 섹션 생성
        const createArticleSection = (title, articles, color) => {
            return `
                <div class="border-l-4 border-${color}-500 pl-4">
                    <h3 class="text-lg font-semibold text-${color}-600 mb-3">${title}</h3>
                    <ul class="space-y-3">
                        ${articles.map(article => `
                            <li>
                                <a href="${article.url}" target="_blank" class="article-link group" data-url="${article.url}">
                                    <strong class="group-hover:text-${color}-600 group-hover:underline transition-colors">${article.title}</strong>
                                    <p class="text-sm text-gray-500">${article.source} (${article.date})</p>
                                    <p class="text-xs text-gray-400 mt-1">${article.summary}</p>
                                </a>
                            </li>
                        `).join('')}
                    </ul>
                </div>
            `;
        };

        // --- 이벤트 핸들러 ---
        
        // 학번/이름으로 로그인 처리
        const handleLogin = (e) => {
            e.preventDefault();
            const studentId = document.getElementById('student-id').value.trim();
            const name = document.getElementById('student-name').value.trim();

            if (!studentId || !name) {
                alert("학번과 이름을 모두 입력해주세요.");
                return;
            }
            
            studentInfo = { studentId, name };
            sessionStorage.setItem('studentInfo', JSON.stringify(studentInfo));
            updateUI();
        };

        // 로그아웃 처리
        const handleLogout = () => {
            studentInfo = null;
            sessionStorage.removeItem('studentInfo');
            updateUI();
        };

        // 기사 클릭 처리
        const handleArticleClick = async (e) => {
            e.preventDefault();
            if (!studentInfo || !firebaseUser) {
                alert("포인트를 적립하려면 먼저 로그인해주세요.");
                return;
            }

            const url = e.currentTarget.dataset.url;
            // [FIX] Firestore 권한 오류 해결을 위해 익명 사용자의 UID를 사용한 개인 경로로 수정
            const userRef = doc(db, `artifacts/${appId}/users/${firebaseUser.uid}/studentProfile/data`);
            
            try {
                const userDoc = await getDoc(userRef);
                const currentPoints = userDoc.exists() && userDoc.data().points ? userDoc.data().points : 0;
                const newPoints = currentPoints + 1;
                
                await setDoc(userRef, { 
                    points: newPoints, 
                    name: studentInfo.name, 
                    studentId: studentInfo.studentId 
                }, { merge: true });

                console.log("포인트 업데이트:", newPoints);
                window.open(url, '_blank');
            } catch (error) {
                console.error("포인트 업데이트 오류:", error);
                window.open(url, '_blank');
            }
        };

        // 모든 기사 링크에 클릭 이벤트 리스너 추가
        const addArticleClickListeners = () => {
            document.querySelectorAll('.article-link').forEach(link => {
                link.addEventListener('click', handleArticleClick);
            });
        };

        // --- Firestore 데이터 리스너 ---

        // 사용자 포인트 실시간 감지
        const listenToUserPoints = (userId) => {
            if (unsubscribeUserPoints) {
                unsubscribeUserPoints();
            }
             // [FIX] Firestore 권한 오류 해결을 위해 익명 사용자의 UID를 사용한 개인 경로로 수정
            const userRef = doc(db, `artifacts/${appId}/users/${userId}/studentProfile/data`);
            unsubscribeUserPoints = onSnapshot(userRef, (doc) => {
                const pointsDisplay = document.getElementById('points-display');
                if (pointsDisplay) {
                    if (doc.exists() && doc.data().points) {
                        pointsDisplay.textContent = `${doc.data().points} P`;
                    } else {
                        pointsDisplay.textContent = '0 P';
                    }
                }
            }, (error) => {
                console.error("Snapshot listener error:", error);
            });
        };

        // --- 앱 초기화 ---
        
        const initializeAppLogic = () => {
            // 페이지 로드 시 sessionStorage 확인하여 로그인 상태 복원
            const storedStudentInfo = sessionStorage.getItem('studentInfo');
            if (storedStudentInfo) {
                studentInfo = JSON.parse(storedStudentInfo);
            }
            updateUI();
            renderTopics();
        };

        // [FIX] Firestore 권한 오류 해결을 위해 익명 인증 상태를 확인하고 앱 로직 실행
        onAuthStateChanged(auth, async (user) => {
            if (user) {
                // 이미 익명 사용자가 있는 경우
                firebaseUser = user;
                initializeAppLogic();
            } else {
                // 익명 사용자가 없는 경우 새로 로그인
                try {
                    const userCredential = await signInAnonymously(auth);
                    firebaseUser = userCredential.user;
                    console.log("익명 로그인 성공:", firebaseUser.uid);
                    initializeAppLogic();
                } catch (error) {
                    console.error("익명 로그인 오류:", error);
                    authContainer.innerHTML = `<p class="text-red-500">서비스에 연결할 수 없습니다. 잠시 후 다시 시도해주세요.</p>`;
                }
            }
        });

    </script>
</body>
</html>
