from useraccount.models import ORMSkill
from useraccount.entities import Skill

class SkillRepo:

    def _decode_db_skill(self, db_skill):
        return Skill(skill_id=db_skill.id,skill_name=db_skill.skill_name)

    def get_all_skill(self):
        all_db_skill = ORMSkill.objects.all()
        skills = []
        for db_skill in all_db_skill:
            skill_.append(self._decode_db_skill(db_skill))
            print(skills)
            return skills
    
    def create_new_skill(self, skill):

        db_skill = ORMSkill.objects.create(skill_name=skill.skill_name)
        

        return self._decode_db_skill(db_skill)

    def update_existing_skill(self,skill):

        db_skill = ORMSkill.objects.get(id = skill.id)
        db_skill.name = skill.name
    
        db_skill.save()
        return self._decode_db_skill(db_skill)

    def delete_existing_skill(self, id):
        return ORMSkill.objects.get(id = id).delete()

    def get_skill(self, id):
        #stdlogger.info("Call to get_skill method")
        #stdlogger.debug("Getting the skill from id")
        db_skill = ORMSkill.objects.get(id = id)
        return self._decode_db_skill(db_skill)