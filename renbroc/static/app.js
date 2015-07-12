RadarChart.defaultConfig.color = function() {};
RadarChart.defaultConfig.radius = 0;
RadarChart.defaultConfig.w = 200;
RadarChart.defaultConfig.h = 200;

var data = [
{
    className: 'stats', // optional can be used for styling
    axes: [
{axis: "topic 1", value: 7},
{axis: "topic 2", value: 6},
{axis: "topic 3", value: 5},
{axis: "topic 4", value: 9},
{axis: "topic 5", value: 2}
]
}
];

var bump_up = [1, 2, 1.5, .5, 1];

var chart = RadarChart.chart();
var cfg = chart.config(); // retrieve default config
var svg = d3.select('#radar-chart').append('svg')
.attr('width', 400)
.attr('height', cfg.h + cfg.h / 4);
svg.append('g').classed('single', 1).attr('transform', 'translate(50, 0)').datum(data).call(chart);

d3.selectAll('text').style('text-anchor', 'middle')
d3.selectAll('.check').on('mouseover', function(d){
    d3.select(this).selectAll("path").style("fill", "#1FBF24");
}).on("mouseout", function(d){
    d3.select(this).selectAll("path").style("fill", "#8e8e8e");
}).on("click", function(d){
    var this_article = this.parentNode;
    d3.select(this.parentNode).remove();
    var cur_id = d3.select(this).attr('id');
    d3.select(this_article).select(".check").remove();
    d3.select("#cat-"+cur_id).insert(function(){
        return this_article;
    }, ":first-child");
    data[0]['axes'][cur_id.replace("a-", "")-1]['value'] += bump_up[cur_id.replace("a-", "")-1];
    svg.datum(data).call(chart);
})
