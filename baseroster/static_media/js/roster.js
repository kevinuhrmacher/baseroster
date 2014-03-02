<script type="text/javascript">



{% for player in player %}
  {% if senior in player.year %}
        document.getElementById('storytabs').innerHTML = '
            <div>
            <ul class="nav nav-tabs">
              <li class="active"><a href="#junior" data-toggle="tab"><span>{{ player.story_junior }} </span></a></li>
              <li><a href="#sophomore" data-toggle="tab"><span>{{ player.story_sophomore }} </span></a></li>
              <li><a href="#freshman" data-toggle="tab"><span>{{ player.story_freshman }} </span></a></li>
              <li><a href="#highschool" data-toggle="tab"><span>{{ player.high_school }}<br>{{ player.story_highschool }} </span></a></li>
              <li><a href="#personal" data-toggle="tab"><span> {{ player.story_personal }} </span></a></li>
            </ul>
            </div>
            
            <div class="row tab-content">
              <div class="tab-pane fade in active" id="junior"><span> {{ player.story_junior }} </span></div>
              <div class="tab-pane fade" id="sophomore"><span> {{ player.story_sophomore }} </span></div>
              <div class="tab-pane fade" id="freshman"><span> {{ player.story_freshman }} </span></div>
              <div class="tab-pane fade" id="highschool"><span> {{ player.story_highschool }} </span></div>
              <div class="tab-pane fade" id="personal"><span> {{ player.story_personal }} </span></div>
            </div>';
        
        {% if junior in player.year %}
        document.getElementById('storytabs').innerHTML = '
            <div>
            <ul class="nav nav-tabs">
              <li class="active"><a href="#sophomore" data-toggle="tab"><span>{{ player.story_sophomore }} </span></a></li>
              <li><a href="#freshman" data-toggle="tab"><span>{{ player.story_freshman }} </span></a></li>
              <li><a href="#highschool" data-toggle="tab"><span> {{ player.high_school }}<br>{{ player.story_highschool }} </span></a></li>
              <li><a href="#personal" data-toggle="tab"><span> {{ player.story_personal }} </span></a></li>
            </ul>
            </div>
            
            <div class="row tab-content">
              <div class="tab-pane fade in active" id="sophomore"><span> {{ player.story_sophomore }} </span></div>
              <div class="tab-pane fade" id="freshman"><span> {{ player.story_freshman }} </span></div>
              <div class="tab-pane fade" id="highschool"><span> {{ player.story_highschool }} </span></div>
              <div class="tab-pane fade" id="personal"><span> {{ player.story_personal }} </span></div>
            </div>';
        
        {}
        
        {% if sophomore in player.year %}
        document.getElementById('storytabs').innerHTML = '
            <div>
            <ul class="nav nav-tabs">
              <li class="active"><a href="#freshman" data-toggle="tab"><span>{{ player.story_freshman }} </span></a></li>
              <li><a href="#highschool" data-toggle="tab"><span> {{ player.high_school }}<br>{{ player.story_highschool }} </span></a></li>
              <li><a href="#personal" data-toggle="tab"><span> {{ player.story_personal }} </span></a></li>
            </ul>
            </div>
            
            <div class="row tab-content">
              <div class="tab-pane fade in active" id="freshman"><span> {{ player.story_freshman }} </span></div>
              <div class="tab-pane fade" id="highschool"><span> {{ player.story_highschool }} </span></div>
              <div class="tab-pane fade" id="personal"><span> {{ player.story_personal }} </span></div>
            </div>';
        
        {% if freshman in player.year %}
        document.getElementById('storytabs').innerHTML = '
            <div>
            <ul class="nav nav-tabs">
              <li class="active"><a href="#highschool" data-toggle="tab"><span> {{ player.high_school }}{{ player.story_highschool }} </span></a></li>
              <li><a href="#personal" data-toggle="tab"><span> {{ player.story_personal }} </span></a></li>
            </ul>
            </div>
            
            <div class="row tab-content">
              <div class="tab-pane fade in active" id="highschool"><li class="active"><a href="#highschool" data-toggle="tab"><span> {{ player.high_school }}{{ player.story_highschool }} </span></a></li></div>
              <div class="tab-pane fade" id="personal"><span> {{ player.story_personal }} </span></div>
            </div>';
 
 
 
 
 
 
 
 
</script>