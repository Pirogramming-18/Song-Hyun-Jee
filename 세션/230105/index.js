/* const date = new Date(); //현재 날짜 객체 만들기
const date2 = new Date(2023, 10, 2); //지정날짜 객체 만들기

/* console.log(date);
console.log(date2); */


/* const viewYear = date.getFullYear();
const viewMonth = date.getMonth();
const viewDate = date.getDate();
const viewDay = date.getDay();

/* console.log(viewYear); //2023
console.log(viewMonth); //0 0~11
console.log(viewDate); //5 -> 1~31
console.log(viewDay); //4  -> 1(월) 2(화) 3(수) */


// 지난 달 마지막 날짜와 요일 
/* const prevLast = new Date(viewYear, viewMonth, 0);
const prevDate = prevLast.getDate();
const prevDay = prevLast.getDay();
 */
/* console.log(prevLast);
console.log(prevDate);
console.log(prevDay); */


// 이번 달 마지막 날짜와 요일
/* const thisLast = new Date(viewYear, viewMonth + 1, 0);
const thisDate = thisLast.getDate();
const thisDay = thisLast.getDay();

console.log(thisLast);
console.log(thisDate);
console.log(thisDay);


const prevDates = []; //[26,27,28,29,30,31]
const nextDates = [];  //[1,...]
/* 
const thisDates = [...Array(thisDate + 1).keys()].slice(1); * */// / [1, 2, 3, ....31] * / */



const date = new Date();
const makeCalendar = () => {
    const viewYear = date.getFullYear();
    const viewMonth = date.getMonth();

    document.querySelector('.year-month').textContent = `${viewYear}년 ${viewMonth + 1}월`

    const prevLast = new Date(viewYear, viewMonth, 0);
    const prevDate = prevLast.getDate();
    const prevDay = prevLast.getDay();

    const thisLast = new Date(viewYear, viewMonth + 1, 0);
    const thisDate = thisLast.getDate();
    const thisDay = thisLast.getDay();

    const prevDates = []; //[26,27,28,29,30,31]
    const thisDates = [...Array(thisDate + 1).keys()].slice(1);
    const nextDates = [];  //[1,...]

    if (prevDay !== 6) {
        for (let i = 0; i < prevDay + 1; i++) {
            prevDates.unshift(prevDate - i);
        }
    }

    for (let i = 1; i < 7 - thisDay; i++) {
        nextDates.push(i);
    }

    //Dates 라는 배열로 모두 합치기
    const dates = prevDates.concat(thisDates, nextDates);

    //div로 감싸서 배열에 넣기
    dates.forEach((date, i) => {
        dates[i] = `<div class="date"> ${date} </div>`;
    });

    //html dates 그리기
    document.querySelector('.dates').innerHTML = dates.join('');
}

makeCalendar();

let date = new Date();

const preMonth = () => {
    date.setDate(1);
    date.setMonth(date.getMonth() - 1);
    makeCalendar();
}

const nextMonth = () => {
    date.setDate(1);
    date.setMonth(date.getMonth() + 1);
    makeCalendar();
}

const curMonth = () => {
    date = new Date();
    makeCalendar();
}

const firstDateIndex = dates.indexOf(1);
const lastDateIndex = dates.indexOf(thisDate);

dates.forach((date, i) => {
    const condition = i >= firstDateIndex && i < lastDateIndex + 1
        ? 'this'
        : 'other';
    dates[i] = `<div class="date"><span class="${condition}">${date}</span></div>`;

})