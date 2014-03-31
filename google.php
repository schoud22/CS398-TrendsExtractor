<?php

class GTrendExtractor
{
    protected $rssUrl;

    public function __construct($rssUrl)
    {
        $this->rssUrl = $rssUrl;
    }

    public function get($format = null)
    {
        $trends = array();
        $matches = array();

        $feed = file_get_contents($this->rssUrl);
        
        foreach (preg_split('/<li>/', $feed) as $i => $list)
        {
            $matches = array();
            if (preg_match('|<a href="([^"]+)">(.+)</a></span></li>|', $list, $matches))
            {
                $trends['trend'][$i] = array($matches[2], $matches[1]);
            }
        }

        return $format == 'json' ? json_encode($trends) : $trends;
    }

}

$gtrend = new GTrendExtractor('http://www.google.com/trends/hottrends/atom/hourly');
$trend = $gtrend->get();
print_r($trend);
