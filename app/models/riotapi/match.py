from ...extensions import db

class MatchModel(db.Model):
    id = db.Column(db.VARCHAR(30), primary_key=True)
    version_id = db.Column(db.VARCHAR(10), db.ForeignKey("version_model.id"))
    continent = db.Column(db.VARCHAR(10))
    creation = db.Column(db.Integer)
    duration = db.Column(db.Integer)
    start = db.Column(db.Integer)
    end = db.Column(db.Integer)
    endedEarlySurrender = db.Column(db.Boolean)

    _participant = db.relationship("ParticipantModel", backref="match_model")
    _team = db.relationship("TeamModel", backref="match_model")

    def __init__(self, **kwargs):
        self.id = kwargs.get("id", None)
        self.version_id = kwargs.get("version_id", None)
        self.continent = kwargs.get("continent", None)
        self.creation = kwargs.get("creation", None)
        self.duration = kwargs.get("duration", None)
        self.start = kwargs.get("start", None)
        self.end = kwargs.get("end", None)
        self.endedEarlySurrender = kwargs.get("endedEarlySurrender", None)
    
    def serialize(self):
        result = {}
        for c in self.__table__.columns.keys():
            result[c] = getattr(self, c)
        
        return result

class TeamModel(db.Model):
    id = db.Column(db.VARCHAR(30), primary_key=True)
    match_id = db.Column(db.VARCHAR(30), db.ForeignKey("match_model.id"))
    key = db.Column(db.VARCHAR(5))
    win = db.Column(db.BOOLEAN)
    first_blood = db.Column(db.BOOLEAN)
    first_turret_kill = db.Column(db.BOOLEAN)
    turret_kills = db.Column(db.INTEGER)
    inhibitor_kills = db.Column(db.INTEGER)
    total_damage_dealt_to_champions = db.Column(db.INTEGER)
    total_damage_taken = db.Column(db.INTEGER)
    kills = db.Column(db.INTEGER)
    deaths = db.Column(db.INTEGER)
    assists = db.Column(db.INTEGER)
    gold_earned = db.Column(db.INTEGER)
    gold_spent = db.Column(db.INTEGER)
    time_CCing = db.Column(db.INTEGER)

    def __init__(self, **kwargs):
        columns = self.__table__.columns
        for k in columns.keys():
            setattr(self, k, kwargs.get(k))

    def serialize(self):
        result = {}
        for c in self.__table__.columns.keys():
            result[c] = getattr(self, c)
        
        return result

class ParticipantModel(db.Model):
    id = db.Column(db.VARCHAR(30), primary_key=True)
    match_id = db.Column(db.VARCHAR(30), db.ForeignKey("match_model.id"))
    key = db.Column(db.INTEGER)
    team_key = db.Column(db.VARCHAR(5))
    puuid = db.Column(db.VARCHAR(100))
    summoner_name = db.Column(db.VARCHAR(50))
    summoner_level = db.Column(db.Integer)
    profileicon_key = db.Column(db.VARCHAR(5))
    champion_key = db.Column(db.VARCHAR(5))
    champion_name = db.Column(db.VARCHAR(20))
    summoner_spell1_key = db.Column(db.VARCHAR(5))
    summoner_spell1_casts = db.Column(db.Integer)
    summoner_spell2_key = db.Column(db.VARCHAR(5))
    summoner_spell2_casts = db.Column(db.Integer)
    spell1_casts = db.Column(db.Integer)
    spell2_casts = db.Column(db.Integer)
    spell3_casts = db.Column(db.Integer)
    spell4_casts = db.Column(db.Integer)
    main_perk1_key = db.Column(db.VARCHAR(5))
    main_perk1_vars = db.Column(db.JSON)
    main_perk2_key = db.Column(db.VARCHAR(5))
    main_perk2_vars = db.Column(db.JSON)
    main_perk3_key = db.Column(db.VARCHAR(5))
    main_perk3_vars = db.Column(db.JSON)
    main_perk4_key = db.Column(db.VARCHAR(5))
    main_perk4_vars = db.Column(db.JSON)
    sub_perk1_key = db.Column(db.VARCHAR(5))
    sub_perk1_vars = db.Column(db.JSON)
    sub_perk2_key = db.Column(db.VARCHAR(5))
    sub_perk2_vars = db.Column(db.JSON)
    shard1_key = db.Column(db.VARCHAR(5))
    shard2_key = db.Column(db.VARCHAR(5))
    shard3_key = db.Column(db.VARCHAR(5))
    item0_key = db.Column(db.VARCHAR(5))
    item1_key = db.Column(db.VARCHAR(5))
    item2_key = db.Column(db.VARCHAR(5))
    item3_key = db.Column(db.VARCHAR(5))
    item4_key = db.Column(db.VARCHAR(5))
    item5_key = db.Column(db.VARCHAR(5))
    item6_key = db.Column(db.VARCHAR(5))
    win = db.Column(db.BOOLEAN)
    kills = db.Column(db.INTEGER)
    deaths = db.Column(db.INTEGER)
    assists = db.Column(db.INTEGER)
    gold_earned = db.Column(db.INTEGER)
    gold_spent = db.Column(db.INTEGER)
    items_purchased = db.Column(db.INTEGER)
    champion_level = db.Column(db.INTEGER)
    champion_transform = db.Column(db.INTEGER)
    champion_experience = db.Column(db.INTEGER)
    total_damage_dealt = db.Column(db.INTEGER)
    total_damage_dealt_to_champions = db.Column(db.INTEGER)
    true_damage_dealt_to_champions = db.Column(db.INTEGER)
    magic_damage_dealt_to_champions = db.Column(db.INTEGER)
    physical_damage_dealt_to_champions = db.Column(db.INTEGER)
    total_damage_taken = db.Column(db.INTEGER)
    true_damage_taken = db.Column(db.INTEGER)
    magic_damage_taken = db.Column(db.INTEGER)
    physical_damage_taken = db.Column(db.INTEGER)
    damage_self_mitigated = db.Column(db.INTEGER)
    time_CCing = db.Column(db.INTEGER)
    total_time_CC_dealt = db.Column(db.INTEGER)
    total_heal = db.Column(db.INTEGER)
    total_heals_on_teammates = db.Column(db.INTEGER)
    total_shielded_on_teammates = db.Column(db.INTEGER)
    time_played = db.Column(db.INTEGER)
    turrets_lost = db.Column(db.INTEGER)
    inhibitors_lost = db.Column(db.INTEGER)
    double_kills = db.Column(db.INTEGER)
    triple_kills = db.Column(db.INTEGER)
    quadra_kills = db.Column(db.INTEGER)
    penta_kills = db.Column(db.INTEGER)
    killing_sprees = db.Column(db.INTEGER)
    largest_multi_kill = db.Column(db.INTEGER)
    largest_killing_spree = db.Column(db.INTEGER)
    bounty_level = db.Column(db.INTEGER)
    total_minions_killed = db.Column(db.INTEGER)
    longest_time_spent_living = db.Column(db.INTEGER)
    total_time_spent_dead = db.Column(db.INTEGER)
    challenges = db.Column(db.JSON)

    def __init__(self, **kwargs):
        columns = self.__table__.columns
        for k in columns.keys():
            setattr(self, k, kwargs.get(k))

    def serialize(self):
        result = {}
        for c in self.__table__.columns.keys():
            result[c] = getattr(self, c)
        
        return result