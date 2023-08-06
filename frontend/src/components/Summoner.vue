<template>
  <div id="summoner"> 
    <div class="summoner-info">
        <div class="summoner-info-wrap">
            <div class="summoner-icon">
                <div class="summoner-icon-wrap">
                    <img src="https://ddragon.leagueoflegends.com/cdn/13.12.1/img/profileicon/5090.png" alt="">
                    <span>157</span>
                </div>
            </div>
            <div class="summoner-name">
                <div class="summoner-name-row">
                    <b>여자맨</b>
                </div>
                <div class="summoner-name-row">
                    <a href="javascript:">전적 갱신</a>
                </div>
                <div class="summoner-name-row">
                    <p>최근갱신: 1분전</p>
                </div>
            </div>
        </div>
    </div>
    <div class="summoner-match">
        <div class="summoner-match-loading" v-if="isLoading == true && matches.length == 0">
            <img src="../assets/image/spinner.gif" alt="">
        </div>
        <ul>
            <li v-for="matchList in summonerMatch" :key="matchList" class="matchList">
                <div class="matchList-wrap-container">
                    <div class="matchList-wrap" :style="`border-left: 8px solid ${ matchList.isWin ? '#5393ca' : '#ed6767' }; background: ${ matchList.isWin ? '#f9fbfd' : '#fef9f9' }`">
                        <div class="match-data">
                            <div class="match-info">
                                <b v-if="matchList.isWin" class="resultWin">승리</b>
                                <b v-else class="resultLose">패배</b>
                                <p>{{ matchList.timeplayedMinutes }}분 {{ matchList.timeplayedSeconds }}초</p>
                                <p>{{ matchList.date }}</p>
                            </div>
                            <div class="summoner-champ">
                                <div class="champ">
                                    <img :src="`http://ddragon.leagueoflegends.com/cdn/13.10.1/img/champion/Aatrox.png`" alt="">
                                    <i>{{ matchList.champLevel }}</i>
                                </div>
                                <div class="spells">
                                    <div class="spell1">
                                        <img src="http://ddragon.leagueoflegends.com/cdn/13.10.1/img/spell/SummonerFlash.png" alt="">
                                    </div>
                                    <div class="spell2">
                                        <img src="http://ddragon.leagueoflegends.com/cdn/13.10.1/img/spell/SummonerFlash.png" alt="">
                                    </div>
                                </div>
                                <div class="runes">
                                    <div class="primaryRune">
                                        <img src="https://ddragon.leagueoflegends.com/cdn/img/perk-images/Styles/Precision/LethalTempo/LethalTempoTemp.png" alt="">
                                    </div>
                                    <div class="subRune">
                                        <img src="https://ddragon.leagueoflegends.com/cdn/img/perk-images/Styles/Precision/LethalTempo/LethalTempoTemp.png" alt="">
                                    </div>
                                </div>
                            </div>                    
                            <div class="summoner-kda">
                                <p class="kda-top">{{ matchList.kills }}/{{ matchList.deaths }}/{{ matchList.assists }}</p>
                                <p v-if="matchList.kda != Infinity" class="kda-bottom">{{ matchList.kda }} KDA</p>
                                <p v-if="matchList.kda == Infinity" class="kda-bottom">Perfect KDA</p>                        
                            </div>
                            <div class="summoner-killGold">
                                <p class="killPercent">킬 관여 <b>100</b>%</p>
                                <p class="goldEarned"><img src="../assets/image/coins.png" alt=""> <b>{{ matchList.goldEarned }}</b></p>
                            </div>   
                            <div class="summoner-items">
                                <ul>
                                    <li class="itemList" v-for="items in matchList.items" :key="items">
                                        <div>
                                            <img v-if="items != Number('0000')" :src="`http://ddragon.leagueoflegends.com/cdn/13.10.1/img/item/${ items }.png`" alt="">
                                        </div>
                                    </li>
                                </ul>
                            </div> 
                        </div>
                        <div class="match-participants">
                            <div class="match-participants-wrap">
                                <ul class="participants-list-container">
                                    <li v-for="blue in 5" :key="blue" class="participants-list">
                                        <div class="participants-list-wrap">
                                            <span class="participants-champ">
                                                <img :src="`http://ddragon.leagueoflegends.com/cdn/13.10.1/img/champion/Aatrox.png`" alt="">
                                            </span>
                                            <p class="participants-name">때리는걸잘해요</p>
                                        </div>
                                    </li>
                                </ul>
                                <ul class="participants-list-container">
                                    <li v-for="red in 5" :key="red" class="participants-list">
                                        <div class="participants-list-wrap">
                                            <span class="participants-champ">
                                                <img :src="`http://ddragon.leagueoflegends.com/cdn/13.10.1/img/champion/Aatrox.png`" alt="">
                                            </span>
                                            <p class="participants-name">때리는걸잘해요</p>
                                        </div>
                                    </li>
                                </ul>
                            </div>
                        </div>
                    </div>
                    <div class="match-detail-open" :style="`background: ${ matchList.isWin ? '#5393ca' : '#ed6767' }`">
                        <a href="javascript:" @click="matchList.openDetail = !matchList.openDetail">
                            <i v-if="matchList.openDetail" class="material-symbols-outlined">expand_less</i>
                            <i v-else class="material-symbols-outlined">expand_more</i>
                        </a>
                    </div>
                </div>
                <div v-if="matchList.openDetail" class="match-detail">
                    <div class="matchList-detail-tab">
                        <ul>
                            <li v-for="(matchDetail,i) in matchDetailTAb" :key="matchDetail">
                                <div>
                                    <a href="javascript:" class="detailTabBtn" :class="{ detailTabClicked: matchList.detailTabOpen[i] }" @click="matchList.detailTabOpen[0] = false, matchList.detailTabOpen[1] = false, matchList.detailTabOpen[2] = false, matchList.detailTabOpen[i] = true">{{ matchDetail }}</a>
                                </div>
                            </li>
                        </ul>
                    </div>
                    <div v-if="matchList.detailTabOpen[0]" class="matchList-detail-table">
                        <div class="detail-table-container">
                            <div class="detail-table-team">
                                <div class="detail-th" :style="`border-top: 1px solid #5393ca; background: #dde9f3`">
                                    <div class="detail-th-wrap">
                                        <p class="detail-th-result" :style="`color: #207ac7`">승리</p>
                                    </div>
                                    <div class="detail-th-wrap">
                                        <p class="detail-th-kda">KDA</p>
                                        <p class="detail-th-damage">
                                            <i class="material-symbols-outlined" @click="matchList.blueDamage = !matchList.blueDamage">arrow_left</i>
                                            <span v-if="matchList.blueDamage">가한 피해량</span>
                                            <span v-else>받은 피해량</span>
                                            <i class="material-symbols-outlined" @click="matchList.blueDamage = !matchList.blueDamage">arrow_right</i>
                                        </p>
                                        <span class="detail-th-kills">
                                            <i class="material-symbols-outlined">swords</i>
                                            <span :style="`color: #207ac7`">50</span>
                                        </span>
                                    </div>
                                </div>
                                <div class="detail-tbody">
                                    <ul class="detail-tbody-wrap">
                                        <li v-for="detailBlueList in matchList.blue" :key="detailBlueList" class="detail-tbody-list" :style="`background: #f9fbfd`">
                                            <div class="detail-tbody-list-wrap">
                                                <div class="detail-content detail-champInfo">
                                                    <div class="detail-champ">
                                                        <img :src="`http://ddragon.leagueoflegends.com/cdn/13.10.1/img/champion/Aatrox.png`" alt="">
                                                        <i>{{ detailBlueList.champLevel }}</i>                                                        
                                                    </div>
                                                    <div class="detail-spells">
                                                        <div class="detail-spell">
                                                            <img src="http://ddragon.leagueoflegends.com/cdn/13.10.1/img/spell/SummonerFlash.png" alt="">
                                                        </div>
                                                        <div class="detail-spell">
                                                            <img src="http://ddragon.leagueoflegends.com/cdn/13.10.1/img/spell/SummonerFlash.png" alt="">
                                                        </div>
                                                    </div>
                                                    <div class="detail-runes">
                                                        <div class="detail-rune">
                                                            <img src="https://ddragon.leagueoflegends.com/cdn/img/perk-images/Styles/Precision/LethalTempo/LethalTempoTemp.png" alt="">
                                                        </div>
                                                        <div class="detail-rune">
                                                            <img src="https://ddragon.leagueoflegends.com/cdn/img/perk-images/Styles/Precision/LethalTempo/LethalTempoTemp.png" alt="">
                                                        </div>
                                                    </div>
                                                </div>
                                                <div class="detail-content detail-name">
                                                    <p>때리는걸잘해요</p>
                                                </div>
                                                <div class="detail-content detail-kda">
                                                    <p class="detail-kda-top">{{ detailBlueList.kills }}/{{ detailBlueList.deaths }}/{{ detailBlueList.assists }}</p>
                                                    <p v-if="detailBlueList.kda != Infinity" class="detail-kda-bottom">{{ detailBlueList.kda }} KDA</p>
                                                    <p v-if="detailBlueList.kda == Infinity" class="detail-kda-bottom">Perfect KDA</p>                        
                                                    
                                                </div>
                                                <div class="detail-content detail-damage">
                                                    <div class="detail-damage-graph" v-if="matchList.blueDamage">
                                                        <p>15,770</p>
                                                        <i :style="`width: 50%`"></i>
                                                    </div>
                                                    <div class="detail-damage-graph" v-else>
                                                        <p>15,770</p>
                                                        <i :style="`width: 70%`"></i>
                                                    </div>
                                                </div>
                                                <div class="detail-content detail-items">
                                                    <ul class="detail-items-wrap">
                                                        <li class="detail-item-list" v-for="blueItems in detailBlueList.items" :key="blueItems">
                                                            <div class="detail-item-list-wrap">
                                                                <img v-if="blueItems != Number('0000')" :src="`http://ddragon.leagueoflegends.com/cdn/13.10.1/img/item/${ blueItems }.png`" alt="">
                                                            </div>
                                                        </li>
                                                    </ul>                                                    
                                                </div>
                                            </div>
                                        </li>
                                    </ul>
                                </div>                           
                            </div>
                            <div class="detail-table-team">
                                <div class="detail-th" :style="`border-top: 1px solid #ed6767; background: #f6e5e5`">
                                    <div class="detail-th-wrap">
                                        <span class="detail-th-kills">
                                            <i class="material-symbols-outlined">swords</i>
                                            <span :style="`color: #ed6767`">50</span>
                                        </span> 
                                        <p class="detail-th-kda">KDA</p>                                        
                                        <p class="detail-th-damage">
                                            <i class="material-symbols-outlined" @click="matchList.redDamage = !matchList.redDamage">arrow_left</i>
                                            <span v-if="matchList.redDamage">가한 피해량</span>
                                            <span v-else>받은 피해량</span>
                                            <i class="material-symbols-outlined" @click="matchList.redDamage = !matchList.redDamage">arrow_right</i>
                                        </p>                                                                               

                                    </div>
                                    <div class="detail-th-wrap">
                                        <span class="detail-th-result" :style="`color: #ed6767`">패배</span>
                                    </div>                                    
                                </div> 
                                <div class="detail-tbody">
                                    <ul class="detail-tbody-wrap">
                                        <li v-for="detailRedList in matchList.red" :key="detailRedList" class="detail-tbody-list" :style="`background: #fef9f9`">
                                            <div class="detail-tbody-list-wrap">
                                                <div class="detail-content detail-champInfo">
                                                    <div class="detail-champ">
                                                        <img :src="`http://ddragon.leagueoflegends.com/cdn/13.10.1/img/champion/Aatrox.png`" alt="">
                                                        <i>{{ detailRedList.champLevel }}</i>                                                        
                                                    </div>
                                                    <div class="detail-spells">
                                                        <div class="detail-spell">
                                                            <img src="http://ddragon.leagueoflegends.com/cdn/13.10.1/img/spell/SummonerFlash.png" alt="">
                                                        </div>
                                                        <div class="detail-spell">
                                                            <img src="http://ddragon.leagueoflegends.com/cdn/13.10.1/img/spell/SummonerFlash.png" alt="">
                                                        </div>
                                                    </div>
                                                    <div class="detail-runes">
                                                        <div class="detail-rune">
                                                            <img src="https://ddragon.leagueoflegends.com/cdn/img/perk-images/Styles/Precision/LethalTempo/LethalTempoTemp.png" alt="">
                                                        </div>
                                                        <div class="detail-rune">
                                                            <img src="https://ddragon.leagueoflegends.com/cdn/img/perk-images/Styles/Precision/LethalTempo/LethalTempoTemp.png" alt="">
                                                        </div>
                                                    </div>
                                                </div>
                                                <div class="detail-content detail-name">
                                                    <p>때리는걸잘해요</p>
                                                </div>
                                                <div class="detail-content detail-kda">
                                                    <p class="detail-kda-top">{{ detailRedList.kills }}/{{ detailRedList.deaths }}/{{ detailRedList.assists }}</p>
                                                    <p v-if="detailRedList.kda != Infinity" class="detail-kda-bottom">{{ detailRedList.kda }} KDA</p>
                                                    <p v-if="detailRedList.kda == Infinity" class="detail-kda-bottom">Perfect KDA</p>                        
                                                    
                                                </div>
                                                <div class="detail-content detail-damage">
                                                    <div class="detail-damage-graph" v-if="matchList.redDamage">
                                                        <p>15,770</p>
                                                        <i :style="`width: 50%`"></i>
                                                    </div>
                                                    <div class="detail-damage-graph" v-else>
                                                        <p>15,770</p>
                                                        <i :style="`width: 70%`"></i>
                                                    </div>
                                                </div>
                                                <div class="detail-content detail-items">
                                                    <ul class="detail-items-wrap">
                                                        <li class="detail-item-list" v-for="redItems in detailRedList.items" :key="redItems">
                                                            <div class="detail-item-list-wrap">
                                                                <img v-if="redItems != Number('0000')" :src="`http://ddragon.leagueoflegends.com/cdn/13.10.1/img/item/${ redItems }.png`" alt="">
                                                            </div>
                                                        </li>
                                                    </ul>                                                    
                                                </div>
                                            </div>
                                        </li>
                                    </ul>
                                </div>                                 
                            </div>
                        </div>
                    </div>
                    <div v-if="matchList.detailTabOpen[1]" class="matchList-detail-build">
                        <div class="matchList-detail-build-wrap">
                            <div class="item-skill-build">
                                <div class="item-build">
                                    <div class="build-header">
                                        <p>아이템 빌드</p>
                                    </div>
                                    <div class="build-content">
                                        <ul class="item-build-list-container">
                                            <li class="item-build-list" v-for="itemBuildList in 10" :key="itemBuildList">
                                                <div class="build-list-arrow">
                                                    <i class="material-symbols-outlined">keyboard_arrow_right</i>
                                                </div>
                                                <div class="build-list-item">
                                                    <div class="build-list-img">
                                                        <div class="build-list-img-wrap">
                                                            <img :src="`http://ddragon.leagueoflegends.com/cdn/13.10.1/img/item/3133.png`" alt="">
                                                        </div>
                                                        <div class="build-list-img-wrap">
                                                            <img :src="`http://ddragon.leagueoflegends.com/cdn/13.10.1/img/item/3133.png`" alt="">
                                                        </div>
                                                    </div>
                                                    <div class="build-list-txt">
                                                        <p>15분</p>
                                                    </div>
                                                </div>
                                            </li>
                                        </ul>
                                    </div>
                                </div>
                                <div class="skill-build">
                                    <div class="build-header">
                                        <p>스킬 빌드</p>
                                    </div>
                                    <div class="build-content skill-master-container">
                                        <div class="skill-build-wrap">
                                            <div class="skill-master">
                                                <ul>
                                                    <li v-for="skillBuild in 3" :key="skillBuild">
                                                        <div class="skill-build-arrow">
                                                            <i class="material-symbols-outlined">keyboard_arrow_right</i>
                                                        </div>
                                                        <div class="skill-build-img">
                                                            <img :src="`https://ddragon.leagueoflegends.com/cdn/13.10.1/img/spell/AatroxQ.png`" alt="">
                                                            <span class="skill-slot">
                                                                <i>Q</i>
                                                            </span>
                                                        </div>
                                                    </li>
                                                </ul>
                                            </div>
                                            <div class="skill-table">
                                                <ul>
                                                    <li v-for="skillTable in 18" :key="skillTable">
                                                        <p class="skill-table-level">18</p>
                                                        <p class="skill-table-slot">Q</p>
                                                    </li>
                                                </ul>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="rune-build">
                                <div class="build-header">
                                    <p>룬 빌드</p>
                                </div>
                                <div class="build-content rune-build-content">
                                    <div class="primary-rune-build">
                                        <div class="rune-build-top">
                                            <span>
                                                <img :src="`https://ddragon.leagueoflegends.com/cdn/img/perk-images/Styles/7201_Precision.png`" alt="">
                                            </span>
                                            <div>
                                                <p>정밀</p>
                                            </div>
                                        </div>
                                        <div class="primary-rune-mid">
                                            <ul>
                                                <li v-for="primaryRuneMid in 4" :key="primaryRuneMid">
                                                    <div>
                                                        <img :src="`https://ddragon.leagueoflegends.com/cdn/img/perk-images/Styles/Precision/Conqueror/Conqueror.png`" alt="">
                                                    </div>
                                                </li>
                                            </ul>
                                        </div>
                                        <div class="rune-img-list">
                                            <div class="rune-img-list-wrap">
                                                <ul v-for="primaryRuneBotContainer in 3" :key="primaryRuneBotContainer">
                                                    <li v-for="primaryRuneBottom in 3" :key="primaryRuneBottom">
                                                        <div>
                                                            <img :src="`https://ddragon.leagueoflegends.com/cdn/img/perk-images/Styles/Precision/Overheal.png`" alt="">
                                                        </div>
                                                    </li>
                                                </ul>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="sub-rune-build">
                                        <div class="rune-build-top">
                                            <span>
                                                <img :src="`https://ddragon.leagueoflegends.com/cdn/img/perk-images/Styles/7201_Precision.png`" alt="">
                                            </span>
                                            <div>
                                                <p>정밀</p>
                                            </div>
                                        </div>
                                        <div class="rune-img-list sub-rune-mid">
                                            <div class="rune-img-list-wrap">
                                                <ul v-for="primaryRuneMidContainer in 3" :key="primaryRuneMidContainer">
                                                    <li v-for="primaryRuneMid in 3" :key="primaryRuneMid">
                                                        <div>
                                                            <img :src="`https://ddragon.leagueoflegends.com/cdn/img/perk-images/Styles/Precision/Overheal.png`" alt="">
                                                        </div>
                                                    </li>
                                                </ul>
                                            </div>
                                        </div>
                                        <div class="rune-img-list sub-rune-bottom">
                                            <div class="rune-img-list-wrap">
                                                <ul v-for="primaryRuneBotContainer in 3" :key="primaryRuneBotContainer">
                                                    <li v-for="primaryRuneBottom in 3" :key="primaryRuneBottom">
                                                        <div class="statmods">
                                                            <img :src="`https://raw.communitydragon.org/latest/plugins/rcp-be-lol-game-data/global/default/v1/perk-images/statmods/statmodsadaptiveforceicon.png`" alt="">
                                                        </div>
                                                    </li>
                                                </ul>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="rune-stat">
                                <div class="build-header">
                                    <p>룬 스탯</p>
                                </div>
                                <div class="build-content">
                                    <ul class="rune-stat-list-container">
                                        <li class="rune-stat-list" v-for="runeStat in 6" :key="runeStat">
                                            <div class="rune-stat-img">
                                                <img :src="`https://ddragon.leagueoflegends.com/cdn/img/perk-images/Styles/7201_Precision.png`" alt="">
                                            </div>
                                            <div class="rune-stat-txt">
                                                <div class="rune-stat-txt-row">
                                                    <p>총 회복량 : <span>1557</span></p>
                                                </div>
                                            </div>
                                        </li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div v-if="matchList.detailTabOpen[2]" class="matchList-detail-teamAnalyze">
                        teamAnalyze
                    </div> 
                </div>                  
            </li>
        </ul>
        <div class="moreBtn" @click="more()" v-if="matches.length">
            <div class="moreBtn-wrap">
                <p v-if="isLoading == false"><i class="material-symbols-outlined">add</i><span>더 보기</span></p>
                <div v-else class="moreSpinner">
                    <img src="../assets/image/spinner.gif" alt="">
                </div>
            </div>
        </div>    
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'summoner',
    data(){
        return{
            matches: [],
            summonerMatch: [],
            matchDetailTAb: ['종합','빌드','팀 분석'],
            isLoading: true,
        }
    },   
    methods: {
        summonerMatchFilter(){
            for( var i=0; i<this.matches.length; i++ ){
                 this.summonerMatch[i] = {
                    items: [],
                    detailTabOpen: [true,false,false],
                    openDetail: false,
                    blueDamage: true,
                    redDamage: true,
                    blue: [{},{},{},{},{}],               
                    red: [{},{},{},{},{}],             
                }
                
                // items
                this.summonerMatch[i].items.push(this.matches[i].myData.item0_id.slice(-4));
                this.summonerMatch[i].items.push(this.matches[i].myData.item1_id.slice(-4));
                this.summonerMatch[i].items.push(this.matches[i].myData.item2_id.slice(-4));
                this.summonerMatch[i].items.push(this.matches[i].myData.item6_id.slice(-4));
                this.summonerMatch[i].items.push(this.matches[i].myData.item3_id.slice(-4));
                this.summonerMatch[i].items.push(this.matches[i].myData.item4_id.slice(-4));
                this.summonerMatch[i].items.push(this.matches[i].myData.item5_id.slice(-4));

                // kda
                this.summonerMatch[i].kills = this.matches[i].myData.kills;
                this.summonerMatch[i].assists = this.matches[i].myData.assists;
                this.summonerMatch[i].deaths = this.matches[i].myData.deaths;
                this.summonerMatch[i].kda = Math.round((this.matches[i].myData.kills+this.matches[i].myData.assists)/this.matches[i].myData.deaths*100)/100;
                
                // gold
                this.summonerMatch[i].goldEarned = this.matches[i].myData.goldEarend.toLocaleString('ko-KR');

                // isWin
                this.summonerMatch[i].isWin = this.matches[i].myData.isWin;
                
                // champLevel
                this.summonerMatch[i].champLevel = this.matches[i].myData.champLevel;

                // time
                var gameStartTime = this.matches[i].gameStartTimeStamp;
                var now = new Date();
                var dataDiff = Math.abs((gameStartTime-now)/(1000*60*60));

                if(dataDiff<24){
                    this.summonerMatch[i].date = `${Math.floor(dataDiff)}시간 전`;
                }
                else{
                    this.summonerMatch[i].date = `${Math.floor(dataDiff/24)}일 전`;
                }                

                // playTime
                var hours = Math.floor(this.matches[i].gameDuration/3600);
                var minutes = Math.floor( (this.matches[i].gameDuration - hours*3600)/60 );
                var seconds = this.matches[i].gameDuration - hours*3600 - minutes*60;

                this.summonerMatch[i].timeplayedMinutes = minutes;
                this.summonerMatch[i].timeplayedSeconds = seconds;    
                
                
                // blue/red
                for( var k=0; k<5; k++ ){
                    this.summonerMatch[i].blue[k].items = [];
                    this.summonerMatch[i].red[k].items = [];

                    // blue kda
                    this.summonerMatch[i].blue[k].kills = this.matches[i].participants[k].kills;
                    this.summonerMatch[i].blue[k].deaths = this.matches[i].participants[k].deaths;
                    this.summonerMatch[i].blue[k].assists = this.matches[i].participants[k].assists;
                    this.summonerMatch[i].blue[k].assists = this.matches[i].participants[k].assists;
                    this.summonerMatch[i].blue[k].kda = Math.round((this.matches[i].participants[k].kills+this.matches[i].participants[k].assists)/this.matches[i].participants[k].deaths*100)/100;

                    // red kda
                    this.summonerMatch[i].red[k].kills = this.matches[i].participants[k+5].kills;
                    this.summonerMatch[i].red[k].deaths = this.matches[i].participants[k+5].deaths;
                    this.summonerMatch[i].red[k].assists = this.matches[i].participants[k+5].assists;
                    this.summonerMatch[i].red[k].kda = Math.round((this.matches[i].participants[k+5].kills+this.matches[i].participants[k+5].assists)/this.matches[i].participants[k+5].deaths*100)/100;

                    // blue champLevel
                    this.summonerMatch[i].blue[k].champLevel = this.matches[i].participants[k].champLevel;

                    // red champLevel
                    this.summonerMatch[i].red[k].champLevel = this.matches[i].participants[k+5].champLevel;

                    // blue items
                    this.summonerMatch[i].blue[k].items.push(this.matches[i].participants[k].item0_id.slice(-4));
                    this.summonerMatch[i].blue[k].items.push(this.matches[i].participants[k].item1_id.slice(-4));
                    this.summonerMatch[i].blue[k].items.push(this.matches[i].participants[k].item2_id.slice(-4));
                    this.summonerMatch[i].blue[k].items.push(this.matches[i].participants[k].item3_id.slice(-4));
                    this.summonerMatch[i].blue[k].items.push(this.matches[i].participants[k].item4_id.slice(-4));
                    this.summonerMatch[i].blue[k].items.push(this.matches[i].participants[k].item5_id.slice(-4));
                    this.summonerMatch[i].blue[k].items.push(this.matches[i].participants[k].item6_id.slice(-4));

                    // red items
                    this.summonerMatch[i].red[k].items.push(this.matches[i].participants[k+5].item0_id.slice(-4));
                    this.summonerMatch[i].red[k].items.push(this.matches[i].participants[k+5].item1_id.slice(-4));
                    this.summonerMatch[i].red[k].items.push(this.matches[i].participants[k+5].item2_id.slice(-4));
                    this.summonerMatch[i].red[k].items.push(this.matches[i].participants[k+5].item3_id.slice(-4));
                    this.summonerMatch[i].red[k].items.push(this.matches[i].participants[k+5].item4_id.slice(-4));
                    this.summonerMatch[i].red[k].items.push(this.matches[i].participants[k+5].item5_id.slice(-4));
                    this.summonerMatch[i].red[k].items.push(this.matches[i].participants[k+5].item6_id.slice(-4));
                }
            }
            this.isLoading = false;
        },
        more(){
            this.isLoading = true;
            axios('http://3.35.8.115/api/search', {
                method: "get",
                params: {
                    name: this.$route.params.id,
                },
            })
            .then( response => {
                let moreMatches = [];
                let originMatches = [];
                moreMatches = response.data;
                originMatches = this.matches;

                this.matches = [...originMatches, ...moreMatches];
                this.summonerMatchFilter();
            })   
            .catch( error => {
                console.log(error);
            });                    
        }
    },
    created(){
        axios('http://3.35.8.115/api/search', {
            method: "get",
            params: {
                name: this.$route.params.id,
            },
        })
        .then( response =>{
            this.matches = response.data;
            console.log(response.data);
            this.summonerMatchFilter();
        })
        .catch( error => {
            console.log(error);
        });      
    },

}
</script>

<style>
@import "../assets/css/reset.css";

#summoner {
    width: 100%; max-width: 1140px;
    margin: 0 auto; 
}

.summoner-info {
    padding: 16px 0;
}

.summoner-info-wrap {
    display: flex;
}

.summoner-icon {
    display: flex;
    margin-right: 20px;
    align-items: center;
}

.summoner-icon-wrap {
    position: relative;
    width: 80px;
    height: 80px;
}

.summoner-icon-wrap img {
    width: 100%;
    border-radius: 50%;    
}

.summoner-icon-wrap span {
    position: absolute;
    bottom: -3px; left: 50%;
    margin-left: -20px;
    display: block;
    width: 40px;
    background: #202d37;
    font-size: 11px;
    color: #fff;
    text-align: center;
    border-radius: 10px;
}

.summoner-name {
    display: flex;
    flex-direction: column;
}

.summoner-name-row {
    display: flex;
    margin-bottom: 12px;
}

.summoner-name-row:last-child {
    margin-bottom: 0px;
}

.summoner-name-row b {
    font-size: 20px;
}

.summoner-name-row a {
    display: block;
    background: #11b288;
    color: #fff;
    height: 40px;
    font-size: 14px;
    line-height: 40px;
    padding: 0 16px;
    font-weight: bold;
}

.summoner-name-row p {
    font-size: 12px;
}

.summoner-match {

}

.summoner-match-loading {
    text-align: center;
}

.summoner-match-loading img {
    width: 32px;
}

.matchList {
    width: 100%;
    margin-bottom: 10px;
    border-top: 1px solid #e6e6e6;
    border-bottom: 1px solid #e6e6e6;
    box-sizing: border-box;
}

.matchList-wrap-container {
    position: relative;
    width: 100%;
    height: 100px;
}

.matchList-wrap {
    display: flex;
    justify-content: space-between;
    height: 100%;
}

.match-data {
    display: flex;
    height: 100%;
    align-items: center;
}

.match-info {
    width: 112px;
    text-align: center;
}

.match-info b {
    font-size: 14px;
}

.match-info p {
    font-size: 12px;
    margin-bottom: 2px;
}

.match-info p:last-child {
    margin-bottom: 0px;
}

.resultWin {
    color: #207ac7;
}

.resultLose {
    color: #ed6767;
}

.summoner-champ {
    display: flex;
}

.champ {
    position: relative;
    width: 52px;
    height: 52px;
    margin-right: 4px;
}

.champ img {
    width: 100%;
}

.champ i {
    position: absolute;
    bottom: 0; right: 0;
    display: block;
    width: 20px;
    height: 20px;
    background: rgba(0,0,0, 0.4);
    color: #fff;
    font-size: 12px;
    font-weight: bold;
    text-align: center;
}

.spells {
    margin-right: 4px;
}

.spells>div {
    width: 24px;
    height: 24px;
}

.spell1 {
    margin-bottom: 4px;
}

.spells>div img {
    width: 100%;
    height: 100%;
}

.runes {

}

.primaryRune {
    margin-bottom: 4px;
}

.runes>div {
    width: 24px;
    height: 24px;
    border-radius: 50%;
    background: #000;
    text-align: center;
}

.primaryRune img {
    width: 20px;
    height: 20px;
    padding: 2px 0;
}

.subRune img {
    width: 16px;
    height: 16px;
    padding: 4px 0;
}

.summoner-kda {
    width: 160px;
    text-align: center;
}

.kda-top {
    font-size: 16px;
    font-weight: bold;
    margin-bottom: 3px;
}

.kda-bottom {
    font-size: 12px;
}

.summoner-killGold {
    width: 120px;
}

.killPercent {
    font-size: 12px;
}

.goldEarned {
    font-size: 12px;
}

.goldEarned img {
    width: 18px;
}

.summoner-items {

}

.summoner-items ul {
    width: 124px;
    display: flex;
    flex-wrap: wrap;
}

.itemList {
    width: 28px;
    height: 28px;
    margin-right: 2px;
    margin-bottom: 2px;
}

.itemList div {
    width: 100%;
    height: 100%;
    background: #e6e6e6;
}

.itemList img {
    width: 100%;
}

.match-participants {
    display: flex;
    padding-right: 30px;
}

.match-participants-wrap {
    display: flex;
    align-items: center;
}

.participants-list-container {
    
}

.participants-list {
    width: 144px;
}

.participants-list-wrap {
    display: flex;
}

.participants-champ {
    display: block;
    width: 14px;
    height: 14px;
    margin-right: 2px;
    margin-bottom: 2px;
}

.participants-champ img {
    width: 100%;
}

.participants-name {
    font-size: 11px;
    line-height: 14px;
    color: #808080;
}

.match-detail-open {
    position: absolute;
    top: 0; right: 0;
    display: block;
    width: 30px;
    height: 100%;
}

.match-detail-open a {
    display: flex;
    justify-content: center;
    align-items: flex-end;
    text-align: center;
    width: 100%;
    height: 100%;
}

.match-detail-open i {
    display: flex;
    color: #fff;
}

.match-detail {
    width: 100%;
    border: 1px solid #e6e6e6;
    border-bottom: 0;
    box-sizing: border-box;
}

.matchList-detail-tab {
    width: 100%;
    background: #fafafa;
}

.matchList-detail-tab ul {
    padding: 9px 16px;
    display: flex;
}

.matchList-detail-tab li {
    display: flex;
}

.detailTabBtn {
    display: block;
    padding: 10px 16px;
    font-size: 12px;
    color: #808080;
}

.detailTabClicked {
    color: #fff;
    background: #363944;
    border-radius: 16px;
}

.matchList-detail-table {
    width: 100%;
}

.detail-table-container {
    display: flex;
    width: 100%;

}

.detail-table-team {
    display: flex;
    flex-grow: 1;
    flex-direction: column;
}

.detail-table-team:first-child {
    border-right: 1px solid #e6e6e6;
}


.detail-th {
    display: flex;
    padding: 0 12px;
    height: 40px;
    justify-content: space-between;
    align-items: center;
}

.detail-th-wrap {
    display: flex;    
}

.detail-th-wrap p {
    display: flex;
    font-size: 12px;
}

.detail-th-result {
    font-weight: bold;
    font-size: 12px;
}

.detail-th-kda {
    width: 62px;
    justify-content: center;
    align-items: center;
}

.detail-th-damage {
    width: 143px;
    justify-content: center;
    align-items: center;
}

.detail-th-damage i {
    cursor: pointer;
}

.detail-th-kills {
    display: flex;
    width: 152px;
    justify-content: flex-end;
    align-items: center;
}

.detail-th-kills i {
    font-size: 16px;
}

.detail-th-kills span {
    font-size: 12px;
}

.detail-table-team:last-child .detail-th-kills {
    display: flex;
    width: 187px;
    justify-content: flex-start;
    align-items: center;
}

.detail-tbody {
    display: flex;
}

.detail-tbody-wrap {

}

.detail-tbody-list {
    border-bottom: 1px solid #e6e6e6;
    box-sizing: border-box;
}

.detail-tbody-list:last-child {
    border-bottom: 0;
}

.detail-tbody-list-wrap {
    display: flex;
    padding: 12px;
}

.detail-content {
    display: flex;
}

.detail-champInfo {
    width: 70px;
    justify-content: space-between;
}

.detail-champ {
    display: flex;
    position: relative;
    width: 34px;
    height: 34px;
}

.detail-champ img {
    width: 100%;
}

.detail-champ i {
    position: absolute;
    bottom: 0; right: 0;
    display: block;
    width: 18px;
    height: 18px;
    background: rgba(0,0,0, 0.4);
    color: #fff;
    font-size: 11px;
    font-weight: bold;
    text-align: center;
}

.detail-spells {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

.detail-spell {
    display: flex;
    width: 16px;
}

.detail-spell img {
    width: 100%;
}


.detail-runes {
    display: flex;
    flex-direction: column;
    justify-content: space-between;    
}

.detail-rune {
    display: flex;
    justify-content: center;
    align-items: center;    
    width: 16px;
    height: 16px;
    background: #000;
    border-radius: 50%;
}

.detail-rune img {
    display: flex;
    width: 12px;

}


.detail-name {
    width: 113px;
    padding-left: 4px;
    align-items: center;
}

.detail-name p {
    display: flex;
    font-size: 11px;
    color: #000;
}

.detail-kda {
    width: 62px;
    flex-direction: column;
    align-items: center;
}

.detail-kda p {
    display: flex;
}

.detail-kda-top {
    font-size: 12px;
    font-weight: bold;
}

.detail-kda-bottom {
    font-size: 11px;
    margin-top: 2px;
}

.detail-damage {
    width: 143px;
    align-items: center;
}

.detail-damage-graph {
    display: flex;
    position: relative;
    width: 100px;
    height: 14px;
    background: #808080;
    margin: 0 auto;
}

.detail-damage-graph p {
    position: relative;
    display: block;
    width: 100%;
    z-index: 2;
    font-size: 12px;
    color: #fff;
    font-weight: bold;
    text-align: center;
    line-height: 14px;
}

.detail-damage-graph i {
    z-index: 1;
    display: block;
    position: absolute;
    top: 0; left: 0;
    width: 50%;
    height: 100%;
    background: #ed6767;
}

.detail-items {
    align-items: center;
}

.detail-items-wrap {
    display: flex;
}

.detail-item-list {
    display: flex;
    width: 20px;
    height: 20px;
    margin-right: 2px;
}

.detail-item-list:last-child {
    margin-right: 0px;
}

.detail-item-list-wrap {
    width: 100%;
    height: 100%;
    background: #e6e6e6;
}

.detail-item-list-wrap img {
    width: 100%;
}

.moreBtn {
    border: 1px solid #999;
    cursor: pointer;
}

.moreBtn-wrap {
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 12px;
}

.moreBtn-wrap p {
    display: flex;
    align-items: center;
}

.moreBtn-wrap span {
    display: flex;
    font-size: 12px;
}

.moreBtn-wrap i {
    display: flex;
    font-size: 18px;
    font-weight: 500;
}

.moreSpinner {
    display: flex;
    width: 18px;
}

.moreSpinner img {
    width: 100%;
}

.matchList-detail-build-wrap {
    display: flex;
}

.build-header {
    display: flex;
    background: #f0f0f0;
    width: 100%;
}

.build-header p {
    color: #000;
    font-size: 12px;
    padding: 10px 12px;
}

.build-content {
    display: flex;
    padding: 16px 14px;
}

.item-skill-build {
    display: flex;
    flex-direction: column;
    flex-grow: 1;
    border-right: 1px solid #e6e6e6;
    box-sizing: border-box;
    width: 472px;
}

.item-build {
    display: flex;
    flex-direction: column;
    width: 100%;
}

.item-build-list-container {
    display: flex;
    flex-wrap: wrap;
    row-gap: 8px;
    width: 100%;
}

.item-build-list {
    display: flex;
}

.item-build-list:first-child .build-list-arrow {
    display: none;
}

.build-list-arrow {
    display: flex;
}

.build-list-arrow i {
    
}

.build-list-item {
    display: flex;
    flex-direction: column;
}

.build-list-img {
    display: flex;
}

.build-list-img-wrap {
    width: 24px;
    margin-right: 2px;
}

.build-list-img-wrap img {
    width: 100%;
}

.build-list-txt {
    display: flex;
    justify-content: center;
}

.build-list-txt p {
    color: #808080;
    font-size: 11px;
}

.skill-build {
    display: flex;
    flex-direction: column;
}

.skill-build-wrap {
    display: flex;
    flex-direction: column;
    row-gap: 12px;
}

.skill-master-container {
    justify-content: center;
}

.skill-master {
    display: flex;
    justify-content: center;
}

.skill-master ul {
    display: flex;
}

.skill-master li {
    display: flex;
}

.skill-master li:first-child .skill-build-arrow {
    display:none;
}

.skill-build-arrow {
    display: flex;
}

.skill-build-arrow i {
    
}

.skill-build-img {
    position: relative;
    display: flex;
    width: 28px;
}

.skill-build-img img {
    width: 100%;
}
.skill-slot {
    position: absolute;
    bottom: 0; right: 0;
    display: flex;
    width: 14px;
    height: 14px;
    background: rgba(0,0,0, 0.7);
    justify-content: center;
    align-items: center;
}

.skill-slot i {
    font-size: 11px;
    color: #fff;
}


.skill-table {
    display: flex;
}

.skill-table ul {
    display: flex;
    border: 1px solid #e6e6e6;
}

.skill-table li {
    display: flex;
    flex-direction: column;
    border-right: 1px solid #e6e6e6;
}

.skill-table li:last-child {
    border-right: 0;
}

.skill-table li p {
    display: flex;
    width: 20px;
    height: 20px;
    font-size: 12px;
    color: #808080;
    justify-content: center;
    align-items: center;
}

.skill-table-level {
    background: #f0f0f0;
}

.skill-table-slot {
    background: #fff;
}

.rune-build {
    display: flex;
    flex-grow: 1;
    flex-direction: column;
    width: 380px;
    border-right: 1px solid #e6e6e6;
    box-sizing: border-box;    
}

.rune-build-content {
    grid-gap: 12px;
}

.primary-rune-build {
    display: flex;
    flex-grow: 1;
    flex-direction: column;
}

.rune-build-top {
    display: flex;
    grid-gap: 8px;
    justify-content: center;
    border-bottom: 1px solid #f0f0f0;
    padding-bottom: 12px;
    margin-bottom: 20px;
}

.rune-build-top span {
    display: flex;
    width: 24px;
}

.rune-build-top img {
    width: 100%;
}

.rune-build-top div {
    display: flex;
    justify-content: center;
    align-items: center;
}

.rune-build-top p {
    font-size: 12px;
    color: #808080;
}

.primary-rune-mid {
    display: flex;
    justify-content: center;
    border-bottom: 1px solid #f0f0f0;
    padding-bottom: 20px;
    margin-bottom: 23px;    
}

.primary-rune-mid ul {
    display: flex;
    width: 148px;
    justify-content: space-between;
}

.primary-rune-mid li {
    display: flex;
}

.primary-rune-mid div {
    width: 28px;
}

.primary-rune-mid img {
    width: 100%;
}

.rune-img-list {
    display: flex;
    justify-content: center; 
}

.rune-img-list-wrap {
    display: flex;
    flex-direction: column;
    row-gap: 16px;
}

.sub-rune-mid .rune-img-list-wrap {
    row-gap: 6px;
}

.sub-rune-bottom .rune-img-list-wrap {
    row-gap: 6px;
}

.rune-img-list-wrap {
    display: flex;
    flex-direction: column;
    row-gap: 16px;
}

.rune-img-list-wrap ul {
    display: flex;
    width: 132px;
    justify-content: space-between;
}

.sub-rune-bottom .rune-img-list-wrap ul {
    width: 108px;
}

.rune-img-list-wrap li {
    display: flex;
}

.rune-img-list-wrap div {
    width: 24px;
}

.rune-img-list-wrap img {
    width: 100%;
}

.rune-img-list-wrap .statmods {
    width: 20px;
    height: 20px;
    border-radius: 50%;
    background: #000;
    display: flex;
    justify-content: center;
    align-items: center;
}

.statmods img {
    width: 100%;
}

.sub-rune-build {
    display: flex;
    flex-grow: 1;
    flex-direction: column;
}

.sub-rune-mid {
    border-bottom: 1px solid #f0f0f0;
    padding-bottom: 15px;
    margin-bottom: 12px;
}

.rune-stat {
    display: flex;
    flex-grow: 1;
    flex-direction: column;
    width: 286px;
}

.rune-stat-list-container {
    display: flex;
    flex-direction: column;
    row-gap: 8px;
}

.rune-stat-list {
    display: flex;
    grid-gap: 8px;
}

.rune-stat-img {
    display: flex;
    align-items: center;
}

.rune-stat-img img {
    width: 28px;
    height: 28px;
}

.rune-stat-txt {
    display: flex;
    flex-direction: column;
    justify-content: center;
    row-gap: 2px;
}

.rune-stat-txt-row {
    display: flex;
}

.rune-stat-txt-row p {
    font-size: 12px;
    color: #646464;
}

.rune-stat-txt-row span {
    color: #000;
}

</style>